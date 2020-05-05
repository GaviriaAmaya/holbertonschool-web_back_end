#!/usr/bin/env python3
"Function that concatenates two strings"


def concat(str1: str, str2: str) -> str:
    "Strictly string concatenation: 'string' + 'another' = 'stringanother'"
    return "{}{}".format(str1, str2)
