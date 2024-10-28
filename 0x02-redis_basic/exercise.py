#!/usr/bin/env python3
"""
exercise.py
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Count the number of time a method is called.

    :method - The method which numbers of calls is counted.

    :rtype - The wrapper/inner function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Increment count of times a method is called.

        :self - Instance of the class
        :args - The arguements to be pass to the method.
        :kwargs - The key word arguement to be pass to the method

        :rtype - The return of the method to be decoreated.
        """
        # Increment the call count in Redis
        if isinstance(self, Cache) and isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)

        # Call the original method and return its result
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache:
    """Definition of class use for caching data."""

    def __init__(self) -> None:
        """
        Initialise a  Cache class by connecting to redis and,
        remove all data in the connected database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
