import logging
from logging.handlers import RotatingFileHandler
import config
import os
import colorlog

class LogHandler:
    """
    A class that handles logging functionality.

    Attributes:
        logger (logging.Logger): The logger object used for logging.
        log_file (str): The path to the log file.

    Methods:
        get_logger(): Returns the logger object.
        get_log_file(): Returns the path to the log file.
        get_log_json(): Returns the log entries in JSON format.
    """

    def __init__(self, name=__name__, level=None, log_file=config.log_file):
        """
        Initializes the LogHandler object.

        Args:
            name (str, optional): The name of the logger. Defaults to __name__.
            level (int, optional): The logging level. Defaults to logging.DEBUG.
            log_file (str, optional): The path to the log file. Defaults to config.log_file.
        """
        if not os.path.exists(config.log_directory):
            os.makedirs(config.log_directory)

        if level is None:
            level = config.min_log_level

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.log_file = log_file

        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=5)

        # Create formatters
        log_format = '%(asctime)s - %(levelname)s - %(name)s - [%(funcName)s] - %(message)s'
        colored_log_format = '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(name)s - [%(funcName)s] - %(message)s'

        # Create colored formatter for console
        colors = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white'
        }
        console_formatter = colorlog.ColoredFormatter(colored_log_format, log_colors=colors, reset=True)

        file_formatter = logging.Formatter(log_format)
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)

        # Add handlers to the logger
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """
        Returns the logger object.

        Returns:
            logging.Logger: The logger object.
        """
        return self.logger
    
    def get_log_file(self):
        """
        Returns the path to the log file.

        Returns:
            str: The path to the log file.
        """
        return self.log_file
    
    def get_log_json(self):
        """
        Returns the log entries in JSON format.

        Returns:
            list: A list of dictionaries representing the log entries in JSON format.
        """
        return_array = []
        #open log file and return json
        with open(self.log_file) as f:
            lines = f.readlines()
            for line in lines:
                split_line = line.split(' - ')
                return_array.append({'date': split_line[0], 'name': split_line[1], 'level': split_line[2], 'function': split_line[3], 'message': split_line[4]})
        
        return return_array


