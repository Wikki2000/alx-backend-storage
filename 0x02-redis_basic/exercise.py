#!/usr/bin/env python3
"""
exercise.py
"""
import redis
from uuid import uuid4
from typing import Union, Callable


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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        Retrieve data from redis database and convert to require type,
        if the optional function is given.

        :param key - The key use to retrieve data in redis database.
        :param fn - The optional function use convert bytes data to any type.
        :rtype - The retrieved data from database, convert if fn is provided.
        """
        data: Union[bytes, None] = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from redis db and convert to str.

        :param key - The key use to retrieved the data.
        :rtype - The string value of retrieved data.
        """
        data: Union[bytes, None] = self._redis.get(key)
        return data.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        Retrieve data from redis db and convert to integer.

        :param key - The key use to retrieved the data.
        :rtype - The string value of retrieved data.
        """
        data: Optional[bytes] = self._redis.get(key)
        return int(data)
