# import logging

# logging.debug('this is debug')
# logging.info('this is info')
# logging.warning('this is waring')
# logging.error('this is error')
# logging.critical('crital')

# logger = logging.getLogger(__name__)


# # create handler

# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # set level

# stream_h.setLevel(logging.warning)
# stream_h.setLevel(logging.error)

# # formatter

# fomatter = logging.Formatter()

# stream_h.setFormatter(fomatter)
# file_h.setFormatter(fomatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warning')
# logger.error('this an error')

import logging
import traceback
try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e,exc_info=True)

# rotating file handler

from logging.handlers import RotatingFileHandler



