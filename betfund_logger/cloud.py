"""Betfund AWS CloudWatch logging utility."""

from boto3.session import Session
from watchtower import CloudWatchLogHandler

from betfund_logger.base import BaseLogger


class CloudLogger(BaseLogger):
    """Class to handle logging to AWS CloudWatch.

    NOTE: Subclasses `betfund_logger.base.BaseLogger`.

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
        aws_access_key: str = None,
        aws_secret_key: str = None,
        aws_region: str = "us-east-1",
        send_interval: int = 15,
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
        """
        super().__init__(log_stream)

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
        self.logger.addHandler(self.handler)
        connection_log = "Connected to AWS CloudWatch (%s): %s (%s)"
        self.logger.info(connection_log, aws_region, log_group, log_stream)

    def __repr__(self):
        """String representation of CloudLogger object."""
        return "<CloudLogger (betfund_logger)>"
