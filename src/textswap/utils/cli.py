"""Command-line interface for the application.

This module defines the CLI argument parser and config file handling.
"""

from pathlib import Path
import argparse


def validate_config_path(path: Path) -> Path:
    """Ensure the config path exists and is a file.

    Used as the `type` for argparse. Raises ArgumentTypeError if invalid.
    """
    path = Path(path).expanduser().resolve()
    if not path.exists():
        raise argparse.ArgumentTypeError(f"Config file not found: {path}")
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"Config path is not a regular file: {path}")
    return path


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the application.

    Returns:
        Parsed arguments with `config` as a Path object.
    """
    parser = argparse.ArgumentParser(
        description="Run the app with a custom config file."
    )

    parser.add_argument(
        "-c",
        "--config",
        type=validate_config_path,
        default="config/config.toml",
        help="Path to the config file (default: config/config.toml)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    # For testing: run this file directly to see cli behavior
    args = parse_args()
    print(f"Using config: {args.config}")
