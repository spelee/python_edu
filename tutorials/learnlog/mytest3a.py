
import logging

# ==============================================================================
# The default logger root is used whenever the logging module's functions are
# called directly.
#
# Define your own logger by creating an object of the Logger class.
# ==============================================================================

# ==============================================================================
# Logger: Class whos objects will be used in the application code directly to
# call the functions
#
# LogRecord: Auto created by Loggers.  Have all the info related to the event
# being logged.
#
# Handler: Send the LogRecord to the required output destination like the
# console or a file.  Its the base for subclasses like StreamHandler,
# FileHandler, SMTPHandler, HTTPHandler
#
# Formatter: Where you specify the format of the output by specifying a string
# format that lists out the attributes that the output should contain.
# ==============================================================================

# ==============================================================================
# Instantiate the Logger class using logging.getLogger(name)
# Multiple calls to getLogger() with the same name will return a reference to
# the same Logger object.
#
# It is recommended that we use module-level loggers by passing __name__ as
# the name parameter to getLogger()
# ==============================================================================


def log_test1():
    logger = logging.getLogger('example_logger')
    logger.warning('This is a warning')
    logger2 = logging.getLogger(__name__)
    logger2.warning('This is another warning')

# ==============================================================================
# Unlike the root logger, custom loggers can't be configured using
# basicConfig()
#
# Like loggers, you can set the severity level in handlers... useful if you
# want to set multiple handlers for the same logger but want different severity
# levels for each of them.  E.g. warnings logged to the console but everything
# to a file.
# ==============================================================================


def log_test2():
    logger = logging.getLogger(__name__)

    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('app.log', mode='w')

    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    c_format = logging.Formatter('%(name)s :: %(levelname)s :: %(message)s')
    f_format = logging.Formatter('%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')

    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning')
    logger.error('This is an error')


# ==============================================================================
# todo: continue with tutorial here...
# https://realpython.com/python-logging/
# Other Configuration methods
# ==============================================================================
def log_test3():
    logger = logging.getLogger(__name__)

    f_handler = logging.FileHandler('app.log', mode='w')

    f_handler.setLevel(logging.DEBUG)

    logger.addHandler(f_handler)

    logger.debug('debug mesg')
    logger.info('info mesg')
    logger.warning('warning mesg')
    logger.error('error mesg')

def log_test4():
    ...

def log_test5():
    ...

def log_test6():
    ...

def log_test7():
    ...

switch = {
    'test1': log_test1,
    'test2': log_test2,
    'test3': log_test3,
    'test4': log_test4,
    'test5': log_test5,
    'test6': log_test6,
    'test7': log_test7
}

runme = 'test3'

switch[runme]()



