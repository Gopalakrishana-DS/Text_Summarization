import os
import logging
import sys

logging_for = "[%(asctime)s: %(name)s: %(levelname)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")

if log_dir != "":
    os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(level=logging.INFO,format = logging_for, 
                    handlers=[logging.StreamHandler(sys.stdout),
                              logging.FileHandler(log_filepath)
                    ]
)
logger = logging.getLogger("Hello")