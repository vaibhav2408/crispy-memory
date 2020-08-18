import logging as logger
import sys

from jira.core.jira_builder import CreateJIRAIssues

"""
Setting up the format of the log message.
"""
fmt_str = '%(asctime)s: [%(threadName)-2.12s] %(levelname)s: [%(filename)s: "%(funcName)s: Line:%(lineno)d] - %(message)s'

"""
Setting the date format for log message
"""
date_str = "%m/%d/%Y %I:%M:%S %p"

"""
Initializing a logger and setting up the format
"""

"""
Adding Handler Filter for Adding Host Name
"""
stream_handler = logger.StreamHandler()

stream_handler.setFormatter(logger.Formatter(fmt_str))

logger.basicConfig(
    handlers=[
        stream_handler],
    level=logger.INFO,
    datefmt=date_str)
logger.info('Setting up logger.')

"""
Calling the executor
The excel sheet file-path must be passed as an input parameter
"""

filepath = sys.argv[1]
CreateJIRAIssues.execute(filepath)
