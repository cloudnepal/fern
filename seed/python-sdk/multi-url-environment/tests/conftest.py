# This file was auto-generated by Fern from our API Definition.

from seed import SeedMultiUrlEnvironment
import os
from seed.environment import SeedMultiUrlEnvironmentEnvironment
import pytest
from seed import AsyncSeedMultiUrlEnvironment


@pytest.fixture
def client() -> SeedMultiUrlEnvironment:
    return SeedMultiUrlEnvironment(
        token=os.getenv("ENV_TOKEN", "token"),
        environment=SeedMultiUrlEnvironmentEnvironment(
            ec_2=os.getenv("TESTS_BASE_URL", "base_url"), s_3=os.getenv("TESTS_BASE_URL", "base_url")
        ),
    )


@pytest.fixture
def async_client() -> AsyncSeedMultiUrlEnvironment:
    return AsyncSeedMultiUrlEnvironment(
        token=os.getenv("ENV_TOKEN", "token"),
        environment=SeedMultiUrlEnvironmentEnvironment(
            ec_2=os.getenv("TESTS_BASE_URL", "base_url"), s_3=os.getenv("TESTS_BASE_URL", "base_url")
        ),
    )
