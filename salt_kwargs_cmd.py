from sh import Command
from functools import wraps

def kwargs_spec(command, arguments, schema):
    def kwargs_spec_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            schema(kwargs)
            f.__globals__['cmd'] = str(Command(command).bake(arguments, **kwargs))
            return f(*args, **kwargs)
        setattr(wrapper, '__annotations__', {'kwargs': schema})
        return wrapper
    return kwargs_spec_decorator
