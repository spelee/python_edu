import logging


# 5 standard logging levels
# DEBUG: Detailed info, typically interesting only when diagnosing problems
# INFO: Confirmation that things are working as expected
# WARNING: Something unexpected happened, or indication of some problem in the near future
# ERROR: A more serious problem that is is preventing the software from performing some function
# CRITICAL: Serious error indicating that the program may be unable to continue running

# Default logging level is WARNING

# logging to a file
# changing the logging level
# changing the formatting of the logging
logging.basicConfig(filename='test.log', level=logging.ERROR,  # level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divid(x, y):
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Subtract: {} + {} = {}'.format(num_1, num_2, sub_result))
logging.error('Subtract: {} + {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Multiply: {} + {} = {}'.format(num_1, num_2, mul_result))

div_result = divid(num_1, num_2)
logging.debug('Divide: {} + {} = {}'.format(num_1, num_2, div_result))

# *** We seem to be UNable to reset the logging config details **
logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.error('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')


