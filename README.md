# betfund-logger
Logger for Betfund.

## Installation

## Usage

```
import os
from betfund_logger import CloudLogger

logger = CloudLogger(
    "log-group-example",
    "log-stream-example",
    os.getenv("AWS_ACCESS_KEY"),
    os.getenv("AWS_SECRET_KEY")
)

logger.info('Hello World, from Betfund Logger!')
```

## Tests