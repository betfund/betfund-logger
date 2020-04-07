# betfund-logger
Logger for Betfund.

## Installation

`pip install git+https://github.com/betfund/betfund-logger.git`

## Usage

### AWS CloudWatch
```
import os
from betfund_logger import CloudLogger

logger = CloudLogger(
    "log-group-example",
    "log-stream-example",
    os.getenv("AWS_ACCESS_KEY"),  # not required if `aws configure`
    os.getenv("AWS_SECRET_KEY"),  # not required if `aws configure`
)

logger.info('Hello World, from Betfund CloudLogger!')
```

### Local File
```
import os
from betfund_logger import LocalLogger

logger = LocalLogger("log-stream-example")

logger.info('Hello World, from Betfund LocalLogger!')
```

## Tests