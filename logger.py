import logging


class Logger(object):
    """Class for logging"""

    def __init__(self, logger_file_name):
        """Class initialization"""

        logging.basicConfig(
                filename=logger_file_name,
                filemode='w',
                level=logging.INFO,
                format='%(asctime)s.%(msecs)d: %(levelname)s-%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')

    """the only 1 instance should exist"""
    _instance = None

    def __new__(self, logger_file_name, *args, **kwargs):
        """Singleton prevents to create another instance"""

        if not self._instance:
            self._instance = super(Logger, self).__new__(self, *args, **kwargs)
        return self._instance

    """Log error message"""
    def error(self, message):
        logging.error(message)

    """Log info message"""
    def info(self, message):
        logging.info(message)
