"""Pytest configuration and fixtures."""

import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.config import settings


@pytest.fixture
def anyio_backend() -> str:
    """Use asyncio backend for pytest-asyncio."""
    return "asyncio"


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create async HTTP client for testing."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def sample_tenant_id() -> str:
    """Sample tenant ID for testing."""
    return "test-tenant-001"


@pytest.fixture
def sample_session_id() -> str:
    """Sample session ID for testing."""
    return "550e8400-e29b-41d4-a716-446655440000"


@pytest.fixture
def sample_image_id() -> str:
    """Sample image ID for testing."""
    return "660e8400-e29b-41d4-a716-446655440001"
