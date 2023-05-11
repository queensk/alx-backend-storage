#!/usr/bin/env python3
"""
Cache storage class
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    counts method call
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, bytes, int, float]:
        """
        wrapper function
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    cache storage information
    """

    def __init__(self):
        """
        create redis instate
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data and return uuid key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """
        Convert the data back to the desired format
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=int)
