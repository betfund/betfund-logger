"""Betfund local logging utility."""

from logging import FileHandler

from betfund_logger.base import BaseLogger


class LocalLogger(BaseLogger):
    """Class to handle local logging.

    NOTE: Subclasses `betfund_logger.BaseLogger`.

    Attributes
    ----------
    logger : logging.Logger
        Main logging object for which to write logs to.
    handler : logging.Handler
        Logging handler for local file logging.
    """

    def __init__(self, log_stream: str):
        """Initialize LocalLogger.

        Parameters
        ----------
        log_stream : str
            Local path to a logging file.
        """
        super().__init__(log_stream)

        # Setup handler and logger objects
        self.handler = FileHandler(log_stream, mode="a+")
        self.logger.addHandler(self.handler)
        connection_log = "Connected to LocalLogger: (%s)"
        self.logger.info(connection_log, log_stream)

    def __repr__(self):
        """String representation of LocalLogger object."""
        return "<LocalLogger (betfund_logger)>"
