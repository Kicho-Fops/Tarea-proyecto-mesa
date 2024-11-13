"""Mesa Agent-Based Modeling Framework.

Core Objects: Model, and Agent.
"""

import datetime

import mesa.experimental as experimental
import mesa.space as space
from mesa.agent import Agent
from mesa.batchrunner import batch_run
from mesa.datacollection import DataCollector
from mesa.model import Model

__all__ = [
    "Model",
    "Agent",
    "space",
    "DataCollector",
    "batch_run",
    "experimental",
]

__title__ = "mesa"
__version__ = "3.1.0.dev"
__license__ = "Apache 2.0"
_this_year = datetime.datetime.now(tz=datetime.UTC).date().year
__copyright__ = f"Copyright {_this_year} Project Mesa Team"