# Duck Javascript Library
# https://github.com/gregglind/duck
# 
# Copyright 2010, Gregg Lind
# Dual licensed under the MIT or GPL Version 2 licenses.
# 

"""use get_logger:
from duck_loggin import get_logger; logger = get_logger(__name__)
# then you can:
logger.debug("foo")
# and if you want to change the logging level:
import logging
logger.parent.setLevel(logging.DEBUG)
"""
from os.path import dirname, join, exists
import logging
import logging.config

logging_conf = join(dirname(__file__), 'logging.conf')
if exists(logging_conf):
    logging.config.fileConfig(logging_conf)
else:
    import sys
    # i'd prefer funcName to lineno, but not available until 2.5
    fmt = "%(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s:%(lineno)d] %(message)s"
    logging.basicConfig(stream=sys.stderr, level=logging.WARNING, format=fmt)

get_logger = logging.getLogger
