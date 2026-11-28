"""Pytest configuration and fixtures for Exportacate backend tests."""

import os
import sys
from pathlib import Path

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Add backend to path for imports
backend_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_root))

from app import create_app, db as _db
from app.config import TestingConfig


@pytest.fixture(scope="session")
def app() -> Flask:
    """Create a Flask app for testing."""
    app = create_app("testing")
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture(scope="function")
def client(app: Flask):
    """Create a test client."""
    return app.test_client()


@pytest.fixture(scope="function")
def db(app: Flask) -> SQLAlchemy:
    """Provide the database for tests."""
    with app.app_context():
        yield _db


@pytest.fixture(scope="function", autouse=True)
def _rollback_db(db: SQLAlchemy):
    """Rollback database changes after each test."""
    yield
    db.session.rollback()