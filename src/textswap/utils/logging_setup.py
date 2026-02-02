#!/usr/bin/env python3
"""Utility to initialize the central logging configuration."""

from pathlib import Path
import logging
import os


def init_logging(project_root: Path = None) -> None:
    """Set up centralized logging to console and file.

    Configures the root logger to write:
      - INFO and above to console
      - DEBUG and above to a file in project_root/logs/app.log

    Args:
        project_root: Project root directory (used for logs/).
    """
    os.environ["PROJECT_ROOT"] = str(project_root)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler: INFO and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # File handler: DEBUG and above
    logs_dir = project_root / "logs"
    logs_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(logs_dir / "app.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    logging.info("Logging initialized!")  # Test root logger
