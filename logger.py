import logging
import functools
"""
Global settings basic config for logging
Setting the format, file output based on level of the message
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create the logging file handler
fh = logging.FileHandler('syncher.log')
fh.setLevel(logging.INFO)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# formatting
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add handler to logger object
logger.addHandler(ch)
logger.addHandler(fh)

"""
Custom formatter, overrides funcName
with value of name_override if it exists"""


class Logged(object):
    """
    Logging decorator that allows you to log with a
    specific logger.
    """

    # Customize these messages
    ENTRY_MESSAGE = 'Entering {}'
    EXIT_MESSAGE = 'Exiting {}'

    def __init__(self, logger=None):
        self.logger = logger

    def __call__(self, func):
        """
        Returns a wrapper that wraps func.
        The wrapper will log the entry and exit points of the function
        with logging.INFO level.
        """

        # set logger if it was not set earlier
        if not self.logger:
            self.logger = logger

        @functools.wraps(func)
        def wrapper(*args, **kwds):
                # logging level .info(). Set to .debug() if you want to
            self.logger.info(self.ENTRY_MESSAGE.format(func.__module__))
            self.logger.info(self.ENTRY_MESSAGE.format(func.__name__))
            f_result = func(*args, **kwds)
            # logging level .info(). Set to .debug() if you want to
            self.logger.info(self.EXIT_MESSAGE.format(func.__name__))
            return f_result
        return wrapper
