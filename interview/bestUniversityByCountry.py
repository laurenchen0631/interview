#!/bin/python3

import math
import os
import random
import re
import sys
import requests



#
# Complete the 'bestUniversityByCountry' function below.
#
# The function is expected to return an STRING.
# The function accepts STRING country as parameter.
# Base URL: https://jsonmock.hackerrank.com/api/universities?page=

cache = {}
def crawlPages() -> dict[str, str]:
    if cache:
        return cache

    university: dict[str, tuple[str, int]] = {}
    total = 1
    page = 1
    while page <= total:
        res = requests.get(f"https://jsonmock.hackerrank.com/api/universities?page={page}")
        data = res.json()
        total = data["total_pages"]
        for uni in data["data"]:
            value = (uni["name"], uni["rank_display"])
            country = uni["location"]["country"]
            if country not in university:
                university[country] = value
            elif university[country][1] > value[1]:
                university[country] = value
        page += 1
    
    for k, v in university.items():
        cache[k] = v[0]
    return cache

def bestUniversityByCountry(country):
    data = crawlPages()
    return data.get(country, "")