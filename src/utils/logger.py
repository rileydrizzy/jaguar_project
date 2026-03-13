"""
This module provides a logger instance using the loguru library. 
The logger is configured to output logs to the console with a specific format, including the timestamp, log level, and message. 
The log level can be adjusted as needed by changing the configuration in this module.

Usage:
- Import the module: `import logger`
- Log messages with different levels:
  - `logger.debug("Debug message")`
  - `logger.info("Informational message")`
  - `logger.warning("Warning message")`
  - `logger.error("Error message")`
  - `logger.critical("Critical message")`
  - `logger.exception("Exception Error")`

"""

from loguru import logger

LOG_FILEPATH = '/logs/app.logs'
FORMAT_STYLE = ()

logger.add(LOG_FILEPATH, format=FORMAT_STYLE, level="INFO",
           rotation="14 days", retention="10 MB", compression="zip")

