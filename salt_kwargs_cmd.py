from sh import Command
from functools import wraps

def kwargs_spec(command, arguments, schema):
    def kwargs_spec_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            kwargs = schema(kwargs)
            for k, v in kwargs.items():
                if k.startswith('--'):
                    del kwargs[k]
                    kwargs[k[2:].replace('-', '_')] = v
            f.__globals__['cmd'] = str(Command(command).bake(
                arguments, **kwargs))
            return f(*args, **kwargs)
        setattr(wrapper, '__annotations__', {'kwargs': schema})
        return wrapper
    return kwargs_spec_decorator
