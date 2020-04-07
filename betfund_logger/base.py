"""Betfund logging utility base class."""

import logging


class BaseLogger:
    """Base class to handle methods of logging.

    Attributes
    ----------
    logger : logging.Logger
        Main logging object for which to write logs to.
    """

    def __init__(
        self,
        log_stream: str,
        formatter="%(asctime)s | %(filename)s (%(lineno)d) | %(levelname)s: %(message)s",
    ):
        """Initialize BaseLogger.

        Parameters
        ----------
        log_stream : str
            Name of the log stream to write logs to.
        formatter : str
            Logging log message format.
        """

        # Setup basic logging configuration
        logging.basicConfig(level=logging.INFO, format=formatter)

        # Setup logger objects
        self.logger = logging.getLogger(log_stream)

    def __repr__(self):
        """String representation of BaseLogger object."""
        return "<BaseLogger (betfund_logger)>"

    def critical(self, message):
        """Write `CRITICAL` log level."""
        self.logger.critical(message)

    def debug(self, message):
        """Write `DEBUG` log level."""
        self.logger.debug(message)

    def error(self, message):
        """Write `ERROR` log level."""
        self.logger.error(message)

    def info(self, message):
        """Write `INFO` log level."""
        self.logger.info(message)

    def warning(self, message):
        """Write `WARNING` log level."""
        self.logger.warning(message)
