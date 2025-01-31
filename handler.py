# Import libraries
import string
import random
from cognite.client.data_classes.data_modeling.ids import *
from cognite.client.data_classes import *
from cognite.client.data_classes.data_modeling import *
from cognite.client.data_classes.data_modeling.data_types import *
from cognite.client.data_classes.filters import*
import os
from cognite.client import CogniteClient
import numpy as np
import pandas as pd
import sys
# from scipy.stats import linregress, skew, kurtosis
from cognite.client.utils import MIN_TIMESTAMP_MS, MAX_TIMESTAMP_MS
import tempfile
import datetime
import operator as op
from cognite.client.data_classes.data_modeling import NodeId
from cognite.client.data_classes import TimeSeriesWrite
from cognite.client.exceptions import CogniteException, CogniteAPIError
from cognite.client.utils import datetime_to_ms
#from cognite.client.utils._time import time_ago_to_ms #TODO: This fn is no longer exists, repalcement accepts '3d' instead of '3d-ago
from cognite.client.utils._time import time_string_to_ms, ms_to_datetime


# Static Variables
functionName = "This a test"

import os
import sys
import logging

from cognite.logger import configure_logger
from cognite.client._version import __version__


# Configure application logger (only done ONCE):
configure_logger(logger_name="func", log_json=False, log_level="INFO")

# The following line must be added to all python modules (after imports):
logger = logging.getLogger(f"func.{__name__}")
logger.info(
    "---------------------------------------START--------------------------------------------"
)
# import importlib
# import inflection


def handle(client):



    logger.info(f"[STARTING] {functionName}")

    
