
import sys
if sys.version_info < (3, 6, 5):
    sys.exit('RoboMaster Sdk requires Python 3.6.5 or later')

import logging
import time

logger_name = "sdk"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.ERROR)

fmt = "%(asctime)-15s %(levelname)s %(filename)s:%(lineno)d %(message)s"
formatter = logging.Formatter(fmt)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)


def enable_logging_to_file():
    logger.setLevel(logging.INFO)
    filename = "RoboMasterSDK_{0}_log.txt".format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    fh = logging.FileHandler(filename)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

from . import action
from . import ai_module
from . import algo
from . import armor
from . import battery
from . import blaster
#from . import camera_ignore
from . import chassis
from . import client
from . import config
from . import conn
from . import dds
from . import event
from . import exceptions
from . import flight
from . import gimbal
from . import gripper
from . import led
from . import media
from . import module
from . import protocol
from . import robot
from . import robotic_arm
from . import sensor
from . import servo
from . import uart
from . import util
from . import version
from . import vision

__all__ = ['logger', 'protocol', 'config', 'version', 'action', 'conn', 'client', 'module',
           'robot', 'gimbal', 'chassis', 'gripper', 'blaster', 'media', 'flight',
           'led', 'robotic_arm', 'vision', 'sensor', 'ai_module', 'algo', 'armor', 'battery', 'dds', 'event',
           'exceptions', 'servo', 'uart', 'util']
