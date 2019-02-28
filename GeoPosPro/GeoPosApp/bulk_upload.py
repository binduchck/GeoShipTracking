import sqlite3
import pandas as pd
import logging
from GeoPosPro import settings

log = logging.getLogger(__name__)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.DatabaseError as ex
        log.error("Connection failed due to {}".format(ex))
    return None

def insert(conn, values):
    """
    Insert ship information into the table GeoApp_shipinfo
    :param conn:
    :param values:
    :return:
    """
    try:
        cur = conn.cursor()
        cur.executemany("INSERT INTO GeoPosApp_shipinfo VALUES (?, ?)", values)
        conn.commit()
    except sqlite3.OperationalError as ex:
        log.error("Operation failed due to {}".format(ex))
        con.rollback()

conn = create_connection("db.sqlite3")

# bulk upload ship's geographical info"

df = pd.read_csv(settings.POSITIONS_FILE, header=None)
df.columns =['id','imo_id', 'position_timestamp', 'latitude', 'longitude']
df.to_sql("GeoPosApp_geoinfo1", conn, if_exists='append', index=False)

#Insert ship info
ship_details = ((9632179, "Mathilde Maersk"), (9247455, "Australian Spirik"),
(9595321, "MSC Preziosa")) ##TODO  should be bulk uploaded or configured
insert(conn, ship_details)

Log.info("Inserted  rows successfuly")
