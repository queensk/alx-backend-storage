#!/usr/bin/env python3
"""
Cache storage class
"""
import redis
from uuid import uuid4
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data and return uuid key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
