import logger
import logging
import os
import sys
from datetime import datetime

# Log file format and path
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
# Create a logs directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")

os.makedirs(log_dir, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
