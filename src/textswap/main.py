from pathlib import Path
import logging
import os

# Best practice: Set environment variable for all modules
os.environ["PROJECT_ROOT"] = str(Path.cwd().resolve())
PROJECT_ROOT = Path(os.environ["PROJECT_ROOT"])

# Import utility functions from your project structure
from textswap.utils.logging_setup import init_logging
from textswap.utils.config import ConfigReader
from textswap.utils.cli import parse_args
from textswap.utils.file_utils import get_index_htmls

# Initialize logging configuration
init_logging(PROJECT_ROOT)
logger = logging.getLogger(__name__)

# Parse command line arguments
args = parse_args()
config_path = args.config

# Load configuration file
config = ConfigReader(config_path)

logger.info("App startet!")  # Application startup log


def main():
    """Main application entry point."""
    BASE_PATH = config.get("path.base_path")

    get_index_htmls(BASE_PATH)
    #py_sed("../../", BASE_PATH, ["/mnt/python/data/index.log"])
    #check_files_from_list("/mnt/python/data/index_mod.log")
if __name__ == "__main__":
    main()