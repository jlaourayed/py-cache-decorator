from typing import Callable


def cache(func: Callable) -> Callable:
    resultats_executions = {}

    def wrapper(*args, **kwargs) -> func:
        cle = (args, tuple(kwargs.items()))
        if cle not in resultats_executions:
            print("Calculating new result")
            resultats_executions[cle] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return resultats_executions[cle]
    return wrapper
