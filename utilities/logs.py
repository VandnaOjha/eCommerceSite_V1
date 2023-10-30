import logging
import os
import datetime

# Define a directory for log files
# log_directory = "logs"
log_directory= "D:\\eCommerceSite_V1\\Logs"

# Create the log directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Generate a timestamp to make the log file unique
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
log_file = os.path.join(log_directory, f"log_{timestamp}.log")
log_format = "%(asctime)s [%(levelname)s] - %(message)s"


class LogGen:
    @staticmethod
    def loggen():
        # # logging.basicConfig(filename="example.log", format='%(asctime)s:%(messages)s',
        # #                     datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        # logging.basicConfig(filename=log_file, format='%(asctime)s:%(messages)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
        logging.basicConfig(
            filename=log_file,
            format=log_format,
            level=logging.INFO  # You can change the logging level as needed
        )

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
