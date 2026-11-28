import os
import warnings
from pathlib import Path

from dotenv import load_dotenv

# Load .env file if present (for local development)
load_dotenv()


def _resolve_database_uri() -> str:
    """
    Resolve database URI from environment.
    - Production: expects DATABASE_URL (PostgreSQL)
    - Development: defaults to SQLite in instance/ folder
    """
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        # Support postgres:// URLs (Heroku/Render style) by converting to postgresql://
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        return database_url

    # Development fallback: SQLite in instance folder
    instance_path = Path(__file__).resolve().parent.parent.parent / "instance"
    instance_path.mkdir(exist_ok=True)
    return f"sqlite:///{instance_path / 'exportacate.db'}"


def _resolve_cors_origins() -> list[str]:
    """
    Resolve allowed CORS origins from FRONTEND_URL.
    - Production: expects FRONTEND_URL (single origin or comma-separated list)
    - Development: defaults to localhost:3000
    """
    frontend_url = os.environ.get("FRONTEND_URL")
    if frontend_url:
        return [origin.strip() for origin in frontend_url.split(",") if origin.strip()]

    # Development default
    return ["http://localhost:3000", "http://127.0.0.1:3000"]


class Config:
    """Base configuration. Values are resolved at class definition time for simplicity,
    but SECRET_KEY validation for production is deferred to create_app()."""

    # SECRET_KEY: set a placeholder; real validation happens in create_app()
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_DATABASE_URI = _resolve_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", "false").lower() == "true"
    CORS_ORIGINS = _resolve_cors_origins()

    @classmethod
    def validate_production(cls) -> None:
        """Validate production-specific settings. Call from create_app()."""
        if os.environ.get("FLASK_ENV") == "production":
            # Check the resolved SECRET_KEY (from .env or environment)
            secret_key = cls.SECRET_KEY
            if not secret_key or secret_key == "dev-secret-key-change-in-production":
                raise RuntimeError(
                    "SECRET_KEY must be set in production environment. "
                    "Generate a secure key with: python -c 'import secrets; print(secrets.token_hex(32))'"
                )
            if cls.SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
                warnings.warn(
                    "Using SQLite in production is not recommended. Set DATABASE_URL to PostgreSQL.",
                    UserWarning,
                    stacklevel=2,
                )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "test-secret-key"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
