import os
import sys
import logging
# there are three important logging functionality need to setup while setting up the logs
# 1. log_dir: where the logs will be stored
# 2. logging_str: format of the logs
# 3. log_filepath: path where the logs will be stored
# 4. logger: logger object which will be used to log the messages
# 5. logging.basicConfig: this will setup the logging configuration
# 6. logging.FileHandler: this will store the logs in the file
# 7. logging.StreamHandler: this will print the logs in the console
# 8. os.makedirs: this will create the directory if it doesn't exist
# 9. logging.getLogger: this will get the logger object 
# 10. logging.INFO: this will set the log level to INFO so that only INFO level logs will be printed


log_dir="logs"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_filepath = os.path.join(log_dir,"continuos_logs.log")

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("summarizerlogger")
