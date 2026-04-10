from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    resultats_executions = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> func:
        sorted_kwargs = tuple(sorted(kwargs.items()))
        cle = (args, sorted_kwargs)
        if cle not in resultats_executions:
            print("Calculating new result")
            resultats_executions[cle] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return resultats_executions[cle]
    return wrapper
