#!/usr/bin/env python3
"""
exercise.py
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
import functools


def replay(method: Callable) -> None:
    """
    Prints the history of calls to the function.

    Parameters:
        method: The function to print the hostory of.
    """
    name = method.__qualname__
    client = redis.Redis()
    inputs = client.lrange("{}:inputs".format(name), 0, -1)
    outputs = client.lrange("{}:outputs".format(name), 0, -1)
    print('{} was called {} times:'.format(name, len(inputs)))
    for input, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, input.decode("utf-8"),
                                     output.decode("utf-8")))


def count_calls(method: Callable) -> Callable:
    """
    Count the number of time a method is called.

    :method - The method which numbers of calls is counted.

    :rtype - The wrapper/inner function.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Increment count of times a method is called.

        :self - Instance of the class
        :args - The arguements to be pass to the method.
        :kwargs - The key word arguement to be pass to the method

        :rtype - The return of the method to be decoreated.
        """
        # Ensure that this is call only when decorator apply to cache class.
        # This prevent error if apply on a class method without self._redis.
        if isinstance(self, Cache) and isinstance(self._redis, redis.Redis):

            # Increment the call count in redis.
            self._redis.incr(method.__qualname__)

        # Call the original method and return its result
        result = method(self, *args, **kwargs)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Keep function call history by cahing it's inputs and output in redis.

    :method - The method to keep track of it call history.
    :rtype - The The wrapper/inner function.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Cache inputs and output of a method in redis.

        :self - Instance of the class.
        :args - The arguements to be pass to the method.
        :kwargs - The key word arguement to be pass to the method.

        :rtype - The return of the method to be decoreated.
        """
        input_list = method.__qualname__ + ":inputs"
        output_list = method.__qualname__ + ":outputs"

        result = method(self, *args, **kwargs)

        if isinstance(self, Cache) and isinstance(self._redis, redis.Redis):
            self._redis.rpush(input_list, str(args))
            self._redis.rpush(output_list, result)

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

    @call_history
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
