#!/usr/bin/env python3
""" Module for filtered logger """
import logging
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """ Function to log filtered data """
    return re.sub(
        f"({'|'.join(fields)})=.*?{separator}",
        lambda m: f"{m.group(1)}={redaction}{separator}",
        message)
