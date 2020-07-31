from contextlib import contextmanager, ContextDecorator
from decimal import *


@contextmanager
def change_decimal_precision(new_precision):
    old_precision = getcontext().prec       # Save old precision
    getcontext().prec = new_precision       # Set a new precision
    yield
    getcontext().prec = old_precision


class ChangeDecimalPrecision(ContextDecorator):
    def __init__(self, new_precision):
        self.old_precision = getcontext().prec
        self.new_precision = new_precision

    def __enter__(self):
        getcontext().prec = self.new_precision
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        getcontext().prec = self.old_precision
