# To keep a log of any execution that happens.
import logging
import os
from datetime import datetime

# Generate a log filename based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

# create a the pathname for logfile, like: src\logs\06_18_2026.log\, nothing is yet added to the system
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# now finally a directory is created, like: src\logs\06_18_2026.log\ , last name if folder name
os.makedirs(logs_path, exist_ok = True)

# Now the log file is added to the above created directory, like
# src\logs\06_18_2026.log\06_18_2026.log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Now that the specific file has been created into the directory, the below function will add the contents.
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, # only message of severity above INFO will be recorded
)