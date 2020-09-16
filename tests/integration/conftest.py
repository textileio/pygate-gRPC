import logging
import os
import shutil
from logging.config import fileConfig
from subprocess import DEVNULL, Popen
from time import sleep, time

import docker
import pytest

from pygate_grpc.client import PowerGateClient
from pygate_grpc.health import HealthClient

fileConfig("logging.ini")

logger = logging.getLogger(__name__)

REPO_LOCAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repo")

pytest_plugins = []


def is_docker_running():
    """Checks if docker is running"""
    logger.debug("Checking if docker is running...")
    client = docker.from_env()
    try:
        client.info()
        return True
    except Exception:
        return False


def is_docker_compose_installed():
    """Checks if docker composed is installed in the system"""
    logger.debug("Checking if docker-compose is installed...")
    proc = Popen(["docker-compose", "help"], stdout=DEVNULL, stderr=DEVNULL)
    proc.communicate()[0]
    return proc.returncode == 0


def clone_powergate_repo():
    """Clones official Powergate repo """
    repo_url = "https://github.com/textileio/powergate"
    logger.debug(f"Cloning powergate repo from {repo_url}")
    Repo.clone_from(repo_url, REPO_LOCAL_PATH, branch="master")


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return [
        os.path.join(REPO_LOCAL_PATH, "docker", "docker-compose-localnet.yaml"),
        os.path.join(REPO_LOCAL_PATH, "docker", "ipfs-image.yaml"),
        os.path.join(REPO_LOCAL_PATH, "docker", "powergate-build-context.yaml"),
    ]


@pytest.fixture(scope="session")
def docker_compose_project_name():
    return "localnet"


def pytest_configure(config):
    """Runs before all tests and makes sure that all the required files
    dependencies are installed in the system"""
    if not is_docker_running():
        logger.error("Coulnd't initiate integration tests. Is Docker running?")
        pytest.exit(3)

    if not is_docker_compose_installed():
        logger.error("Coulnd't initiate integration tests. Is docker-compose installed?")
        pytest.exit(3)

    clone_powergate_repo()


def pytest_unconfigure(config):
    """Runs before test process exits. Cleans up any artifacts from configure"""
    try:
        shutil.rmtree(REPO_LOCAL_PATH)
    except OSError:
        logger.warning("Couldn't delete powergate repository. Maybe it wasn't cloned in the first place")


@pytest.fixture(scope="session", autouse=True)
def localnet(docker_services):
    """Starts a cli container to interact with localnet"""
    client = docker.from_env()
    container = client.containers.run(
        "pygate/powergate-cli:v0.0.1-beta.13",
        network_mode="host",
        auto_remove=True,
        detach=True,
        tty=True,
    )
    start_time, timeout = time(), 600
    while True:
        if time() - start_time > timeout:
            logger.error("Setting up localnet timed out....")
            pytest.exit(3)

        sleep(5)

        try:
            result = container.exec_run("pow health")
            if result.exit_code > 0:
                continue
        except docker.errors.ContainerError:
            continue
        break

    yield {"cli": container}

    logger.debug("Tearing down localnet...")
    container.stop()


@pytest.fixture(scope="session")
def pygate_client():
    return PowerGateClient("127.0.0.1:5002")


@pytest.fixture(scope="session")
def pygate_health_client():
    return HealthClient("127.0.0.1:5002")
