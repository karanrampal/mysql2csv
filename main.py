#!/usr/bin/env python3
"""Test mysql"""

import argparse
import mysql.connector as mysql

def args_parse():
    """Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',
                        '--data_dir',
                        default=None,
                        help="Directory containing the database")
    return parser.parse_args()

def main():
    """Main function
    """
    pass

if __name__ == "__main__":
    main()
