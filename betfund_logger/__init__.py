"""Betung logging utility."""

import logging

from boto3.session import Session
from watchtower import CloudWatchLogHandler


class CloudLogger:
    """Class to handle logging to AWS CloudWatch.

    Attributes
    ----------
    logger : logging.Logger
        Main logging object for which to write logs to.
    handler : logging.Handler
        Logging handler for AWS CloudWatch and formatting.
    """

    def __init__(
        self,
        log_group: str,
        log_stream: str,
        aws_access_key: str,
        aws_secret_key: str,
        aws_region: str = "us-east-1",
        send_interval: int = 15,
        formatter="%(asctime)s | %(filename)s (%(lineno)d) | %(levelname)s: %(message)s",
    ):
        """Initialize CloudLogger.

        Parameters
        ----------
        log_group : str
            Name of the CloudWatch log group to write logs to.
        log_stream : str
            Name of the CloudWatch log stream to write logs to.
        aws_access_key : str
            AWS Access Key ID from AWS management console.
        aws_secret_key : str
            AWS Secret Access Key from AWS management console.
        aws_region : str
            AWS Region used for Amazon CloudWatch.
        send_interval : int
            Maximum seconds to hold messages in queue before sending a batch.
        formatter : str
            Logging log message format.
        """

        # Setup basic logging configuration
        logging.basicConfig(level=logging.INFO, format=formatter)

        # Connect to AWS Session through boto3
        boto3_session = Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region,
        )

        # Setup handler and logger objects
        self.handler = CloudWatchLogHandler(
            log_group=log_group,
            stream_name=log_stream,
            boto3_session=boto3_session,
            send_interval=send_interval,
            create_log_group=False,
            create_log_stream=False,
        )
        self.logger = logging.getLogger(log_stream)
        self.logger.addHandler(self.handler)
        self.logger.info("Connected to AWS CloudWatch: %s (%s)", log_group, log_stream)

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


__all__ = ["CloudLogger"]
