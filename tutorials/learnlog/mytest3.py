
import logging

# ==============================================================================
# By default, there are 5 standard levels indicating the severity of events.
# The logging module provides you with a default logger.
# By default, the logging module only logs severity levels of WARNING or above.
# root is the name the logging module gives to its default logger.
# ==============================================================================


def log_test1():
    logging.debug('Lvl 1: This is a debug message')  # will not log
    logging.info('Lvl 2: This is an info message')  # will nog log
    logging.warning('Lvl 3: This is a warning message')
    logging.error('Lvl 4: This is an error message')
    logging.critical('Lvl 5: This is a critical message')

# ==============================================================================
# You can use the basicConfig(**kwargs) method to configure logging
#
# It should be noted that calling basicConfig() to configure the root logger
# only works if the root logger has not been configured before.
#
# debug(), info(), warning(, error(), and critical() also call basicConfig()
# without arguments automatically if it has not been called before.  So after
# the first time one of the above functions is called, you can no longer
# the root logger.
#
# level: Log at or above the specified level
# ==============================================================================


def log_test2():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Lvl 1: This is a debug message')  # will not log
    logging.info('Lvl 2: This is an info message')  # will nog log
    logging.warning('Lvl 3: This is a warning message')
    logging.error('Lvl 4: This is an error message')
    logging.critical('Lvl 5: This is a critical message')

# Will not set level to logging.DEBUG because logging.info() (and therefore
# basicConfig has already been called


def log_test3():
    logging.warning('This is a warning message')  # will nog log
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Lvl 1: This is a debug message')  # will not log

# ==============================================================================
# filename: To specify the file
# filemode: If filename is given, the file is opened in this mode.  The default is a ('append')
# format: Format of the log message
#
# more params here: https://docs.python.org/3/library/logging.html#logging.basicConfig
# ==============================================================================


def log_test4():
    logging.basicConfig(filename='app.log', filemode='w',
                        format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
    logging.warning('This is a warning and should get logged to a file')

# ==============================================================================
# formatting using {} (str.format())
# Note that style='}'
# And also date formatting, which uses the same formatting language found
# in the datetime module.
# ==============================================================================


def log_test5():
   logging.basicConfig(filename='app.log',
                       filemode='a',
                       format='{asctime} :: {process:,.3f} :: {levelname} :: {message}',
                       datefmt='%d-%b-%y %H:%M:%S',
                       style='{')
   logging.error('Formatting...')

# ==============================================================================
# https://docs.python.org/3/howto/logging-cookbook.html#use-of-alternative-formatting-styles
#
# Including dynamic data... simply pass as positional arguments to the actual
# logging method (i.e. info(), warning(), etc).  (Keyword params to the logging
# method are used for determining options for how to handle the actual logging
# call.)
#
# So cannot include str.format() or string.Template syntax when making logging
# calls.
#
# Note: Actual formatting is delayed until it is necessary.  For example, if
# DEBUG messages are not logged then the formatting is not performed at all.
# (If you passed a pre-formatted sting to the logging method, this would not be
# the case, I think.  That is formatting occurs regardless.  Worth keeping in
# mind if performance is a consideration I think.)
# ==============================================================================


def log_test6():
    context = {'which': 'test6', 'feature': 'logging methods'}
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s :: %(levelname)s :: %(which)s-%(feature)s :: %(message)s',
                        datefmt='%H:%M:%S')
    logging.info('%s %d %f', 'mystring', 77, 3.6, extra=context)
    logging.warning('%(long)s %(short)d', {'long': 'MSFT', 'short': 556}, extra=context)
    logging.warning('super%s', 'woman', stack_info=True, extra=context )
    logging.warning('super%s', 'man', exc_info=True, extra=context)
    logging.warning('peek a boo baby', extra={'which': 'new', 'feature': 5})


# ==============================================================================
# Capturing stack traces
#
# Also, logging.exception() is like logging.error(exc_info=True)
# ==============================================================================


def log_test7():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s :: %(levelname)s :: %(message)s',
                        filename='app.log', filemode='w',
                        datefmt='%H:%M%S')
    logging.debug('my msg', exc_info=True)

    try:
        a = 5 / 0
        print(a)
    except Exception as e:
        logging.debug('my other msg', exc_info=e)

    logging.warning('Arrived here now')

    try:
        a = 10/0
        print(a)
    except Exception as f:
        logging.debug('my third msg', exc_info=True)
    logging.error('Final destination')

    logging.exception('(1) Never mind, this is the absolute last')

    try:
        a = 3/0
        print(a)
    except ZeroDivisionError:
        logging.exception('(2) Never mind, this is the absolute last')


switch = {
    'test1': log_test1,
    'test2': log_test2,
    'test3': log_test3,
    'test4': log_test4,
    'test5': log_test5,
    'test6': log_test6,
    'test7': log_test7
}

runme = 'test7'

switch[runme]()



