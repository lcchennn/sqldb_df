import sqlite3
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def readtodf(path):
    df = pd.read_csv(path)
    return df

def readfromdb(dbname, tablename):
    df = 0
    try:
        conn = sqlite3.connect(dbname, detect_types=sqlite3.PARSE_COLNAMES)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + tablename)
        r = cur.fetchone()
        column_name = r.keys()

        cur = conn.cursor()
        cur.execute("SELECT * FROM " + tablename)
        df = pd.DataFrame(cur.fetchall(), columns=column_name)
        conn.close()

    except Exception as e:
        print(e)
    return df


def dftosqldb(df, tablename, dbname):
    disk_engine = create_engine(r'sqlite:///' + dbname + '.db')
    df.to_sql(tablename, disk_engine, if_exists='append')
    return disk_engine

def dftosqlfile(df, tablename, sqlfilename):
    disk_engine = create_engine(r'sqlite:///' + sqlfilename + '.sqlite')
    df.to_sql(tablename, disk_engine, if_exists='append')
    return disk_engine

def common_column(df1, df2):
    c = np.intersect1d(df2.columns, df1.columns)
    return c

def npercnetile(df, input_pct):
    npct = {}
    for i in df.columns:
        try:
            npct[i] = [np.percentile(df[i], input_pct)]
        except:
            continue
    return npct
