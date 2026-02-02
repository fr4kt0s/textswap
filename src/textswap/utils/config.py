#!/usr/bin/env python3
"""
ConfigReader: Loads and manages a YAML configuration file (DEBUG version).
"""


import logging
import os
from pathlib import Path
import yaml


logger = logging.getLogger(__name__)


def get_project_root() -> Path:
    """Return the project root directory by searching for pyproject.toml.

    Walks upward from the current file until pyproject.toml is found.
    Raises:
        RuntimeError: If pyproject.toml is not found in any parent directory.
    """
    path = Path(__file__).resolve()

    while path.parent != path:
        if (path / "pyproject.toml").exists():
            root = path.resolve()
            return root
        path = path.parent

    raise RuntimeError("pyproject.toml not found!")


class ConfigReader:
    """Loads and provides access to a YAML config file using dot notation."""

    def __init__(self, config_path: str = "config/config.toml") -> None:
        """Initialize ConfigReader with a relative config file path.

        Args:
            config_path: Path to config file (relative to project root).
        """
        # Determine project root from env var or auto-discovery
        self.project_root = Path(os.environ.get("PROJECT_ROOT", get_project_root()))

        # Build full config path
        full_path = self.project_root / config_path
        if not full_path.exists():
            print(f"❌ ERROR: {full_path} not found!")
            print(f"   Create config/config.toml from config.example.yaml!")
            raise FileNotFoundError(f"Create {full_path}!")

        # Load YAML config
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                self.config = yaml.safe_load(f)
            logger.info(f"Config loaded: {full_path}")
        except yaml.YAMLError as e:
            print(f"❌ YAML error: {e}")
            logger.error(f"YAML error: {e}")
            raise

    def get(self, key: str, default=None):
        """Get a config value using dot notation (e.g., 'logging.level').

        Args:
            key: Dot-separated key path (e.g., 'project.name').
            default: Value to return if key is not found.

        Returns:
            The config value at the given key, or default if not found.
        """
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                logger.warning(f"Config '{key}' → using default")
                return default

        return value

    def __getitem__(self, key):
        """Allow dict-style access: config['project.name']."""
        return self.get(key)

    def __repr__(self):
        """String representation of ConfigReader for debugging."""
        return f"<ConfigReader: {self.project_root / 'config/config.toml'}>"
