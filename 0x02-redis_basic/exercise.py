#!/usr/bin/env python3
"""
exercise.py
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Definition of class use for caching data."""

    def __init__(self) -> None:
        """
        Initialise a  Cache class by connecting to redis and,
        remove all data in the connected database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store in redis db data using uuid4 str as key.

        :param data - Data to be stored in redis database.
        :rtype - The key of the data stored in databse.
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
