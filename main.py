#!/usr/bin/env python3
"""Test mysql"""

import argparse
import sys
import getpass
import mysql.connector as mysql
import pandas as pd

def args_parse():
    """Parse command line arguments
    """
    parser = argparse.ArgumentParser(description="Save mysql database as csv file")
    parser.add_argument('-u',
                        '--username',
                        default="root",
                        help="Username to connect to the database server")
    parser.add_argument('-n',
                        '--hostname',
                        default="localhost",
                        help="Server location")
    parser.add_argument('-d',
                        '--data_path',
                        default="ml_mimo",
                        help="Directory containing the database")
    return parser.parse_args()

def main():
    """Main function
    """
    args = args_parse()

    try:
        password = getpass.getpass()
    except ValueError as error:
        sys.exit('Error: {0}'.format(error))

    cnx = mysql.connect(user=args.username,
                        password=password,
                        host=args.hostname,
                        database=args.data_path)

    events_df = pd.read_sql("SELECT * FROM events", cnx)
    print(events_df.head())

    cnx.close()


if __name__ == "__main__":
    main()
