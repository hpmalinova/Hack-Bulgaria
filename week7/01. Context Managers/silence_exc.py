from contextlib import contextmanager, ContextDecorator

default_exc_msg = 'Test'


@contextmanager
def silence_exception(expected_exc_type, expected_exc_msg=default_exc_msg):
    try:
        yield
    except Exception as caught_exc:
        if type(caught_exc) != expected_exc_type or \
           str(caught_exc) != expected_exc_msg:
            raise type(caught_exc)(str(caught_exc))


class silence_exception_class(ContextDecorator):
    def __init__(self, exc_type, exc_msg=default_exc_msg):
        self.expected_exc_type = exc_type
        self.expected_exc_msg = exc_msg

    def __enter__(self):
        return self

    def __exit__(self, caught_exc_type, caught_exc_value, traceback):
        same_type = self.expected_exc_type == caught_exc_type
        same_message = caught_exc_value is not None and \
            self.expected_exc_msg == str(caught_exc_value)

        return same_type and same_message
