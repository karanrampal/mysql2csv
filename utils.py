#!/usr/bin/env python3
"""Utility functions"""

import os

def mkdir_safe(path):
    """Make directory safely
    Args:
        path: (string) Path to make directory
    """
    if os.path.exists(path):
        print("Directory already exists!")
    else:
        print("Making directory!")
        os.mkdir(path)
