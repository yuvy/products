import sqlite3
import os
import csv
import sys

from collections import OrderedDict

DB_PATH = os.path.join(os.path.dirname(__file__), 'app', 'data.db')
DEFAULT_FILE_NAME = 'products.csv'


def ingest_db_data(csv_file=None):
    """
    Ingest data from csv file to SQLLite DB

    :param csv_file: CSV file to ingest Data from, if not supplied uses default file
    :return:
    """

    # Read contents from CSV file and extract data for DB upload
    with open(csv_file or DEFAULT_FILE_NAME) as fp:
        d = csv.DictReader(fp)

        data = []

        # Data formatting, removing spaces from strings
        for x in d:
            t = OrderedDict()
            for k, v in x.items():
                t[k.strip(' ')] = v.replace('"', '').strip(' ')
            data.append(t)

        # Delete temp dict data
        del d

        # Prepare data for uploading on DB
        db_data = [(i['Id'], i['Name'], i['Brand'], i['Retailer'], i['Price'], i['InStock']) for i in data]

    # Connect to SQlLite DB
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS prods;")

    cur.execute("CREATE TABLE IF NOT EXISTS prods (SNo INTEGER PRIMARY KEY, Id INTEGER, Name TEXT, Brand TEXT, "
                "Retailer TEXT, Price INTEGER, InStock TEXT);")

    cur.executemany("INSERT INTO prods (Id, Name, Brand, Retailer, Price, InStock) "
                    "VALUES (?, ?, ?, ?, ?, ?);", db_data)

    # commit and close db connection
    con.commit()
    con.close()

    print('- Done -')


if __name__ == "__main__":

    args = sys.argv

    if len(args) > 1:
        csv_file_name = args[1]
    else:
        print("No CSV File supplied, using default file: ", DEFAULT_FILE_NAME)
        csv_file_name = DEFAULT_FILE_NAME

    ingest_db_data(csv_file_name)

