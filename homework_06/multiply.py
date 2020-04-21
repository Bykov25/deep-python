#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import cProfile


logger = logging.getLogger("Logger")
logger.setLevel(logging.ERROR)
logger.setLevel(logging.INFO)
file = logging.FileHandler("logs.txt")
file.setFormatter(logging.Formatter("[%(asctime)s] - %(levelname)s - %(message)s"))
logger.addHandler(file)

def get_profile(func):
    def wrapper(*args, **kwargs):
        filename = func.__name__ + '.prof'
        pr = cProfile.Profile()
        result = pr.runcall(func, *args, **kwargs)
        pr.dump_stats(filename)
        return result
    return wrapper


def arg_validation(lst):
    if not isinstance(lst, list):
        msg = "Function argument is not a list"
        logger.error(f"multiply({lst}) -> " + msg)
        raise TypeError(msg)
    if len(lst) == 0:
        msg = "Empty list"
        logger.error(f"multiply({lst}) -> function argument - " + msg)
        raise ValueError(msg)
    if len(lst) == 1:
        msg = "List consists of one element"
        logger.error(f"multiply({lst}) -> " + msg)
        raise ValueError(msg)
    for item in lst:
        if not isinstance(item, (int, float)):
            msg = "List contains not a number"
            logger.error(f"multiply({lst}) -> " + f"{item} not a number")
            raise TypeError(msg)
    return True

@get_profile
def multiply(lst):
    if not arg_validation(lst):
        return
    pref = []
    suff = []
    result = []
    pref.append(1)
    for i in range(len(lst)):
        item = pref[i] * lst[i]
        pref.append(item)
    suff.append(1)
    for i in range(len(lst)):
        item = suff[i] * lst[len(lst) - i - 1]
        suff.append(item)
    for i in range(len(lst)):
        item = pref[i] * suff[len(lst) - i - 1]
        result.append(item)
    logger.info((f"The function is called with the following argument: {lst}\n") + 
                (f"Prefix list: {pref}\nSuffix list: {suff}\nresult list: {result}"))
    return result
