import traceback
import inspect
import sys
from functools import wraps


def message_compose(err_type, err_message, err_code, err_description):
    return f"""Hey ChatGPT! I have the following {err_type}: {err_message}.
The failing line is: {err_code}
Description: {err_description}
How can I improve my code to fix this error??
"""


def capture_stderr(err_description=''):
    def wrapper(func):
        @wraps(func)
        def wrapped_args(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                err_type = type(e).__name__
                err_message = str(e)

                tb = traceback.extract_tb(sys.exc_info()[2])
                last_frame = tb[-1]

                err_code = last_frame.line

                message = message_compose(
                    err_type,
                    err_message,
                    err_code,
                    err_description
                )

                print(message)
                raise
        return wrapped_args
    return wrapper


@capture_stderr("Computes factorial of a number")
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f
