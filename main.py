#!/usr/bin/env python3
"""Read mysql database and save the tables as csv files"""

import os
import argparse
import sys
import getpass
import mysql.connector as mysql
import pandas as pd
from utils import mkdir_safe

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
                        '--database',
                        default="ml_mimo",
                        help="Name of the database")
    parser.add_argument('-o',
                        '--output_dir',
                        default="./",
                        help="Directory to write the table csv files")
    return parser.parse_args()

def main():
    """Main function
    """
    args = args_parse()

    # Get password for the mysql server
    try:
        password = getpass.getpass()
    except ValueError as error:
        sys.exit('Error: {0}'.format(error))

    # Connect to the mysql server using python-db api
    cnx = mysql.connect(user=args.username,
                        password=password,
                        host=args.hostname,
                        database=args.database)

    # Tables to read from the database
    tables = ['cells', 'headers', 'events']

    mkdir_safe(args.output_dir)

    for table in tables:
        print("Reading {0} table ...".format(table))
        data_frame = pd.read_sql("SELECT * FROM {0}".format(table), cnx)

        print("Writing {0} table ...".format(table))
        data_frame.to_csv(os.path.join(args.output_dir, table + '.csv'))
        #data_frame.to_parquet(os.path.join(args.output_dir, table + '.parquet'),
        #                      engine='pyarrow',
        #                      compression=None)

    print("Done ...")

    cnx.close()


if __name__ == "__main__":
    main()
