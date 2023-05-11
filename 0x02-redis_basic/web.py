#!/usr/bin/env python3
"""
create a web cache
"""
import requests
import redis
from functools import wraps
from typing import Callable, Union

redis_client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    count calls
    """
    @wraps(method)
    def wrapper(url: str) -> Union[str, None]:
        """
        wraps function
        """
        count_key = "count:{}".format(url)
        result_key = "result:{}".format(url)

        cached_result = redis_client.get(result_key)
        if cached_result:
            redis_client.incr(count_key)
            return cached_result.decode("utf-8")

        response = requests.get(url)
        html_content = response.text

        redis_client.setex(result_key, 10, html_content)
        redis_client.set(count_key, 1)

        return html_content


@count_calls
def get_page(url):
    return requests.get(url).text
