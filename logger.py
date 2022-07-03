import logging


class Logger(object):
    """Class for logging"""

    def __init__(self, logger_file_name):
        """Class initialization"""

        if logger_file_name:
            logging.basicConfig(
                filename='app.log',
                filemode='w',
                level=logging.INFO,
                format='%(asctime)s.%(msecs)d: %(levelname)s-%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
        else:
            logging.basicConfig(
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

    def error(self, message):
        """Log error message"""

        logging.error(message)

    def info(self, message):

        """Log info message"""
        logging.info(message)
