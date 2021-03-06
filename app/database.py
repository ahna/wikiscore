# -*- coding: utf-8 -*-
"""
Database connection utility functions
@author: ahna
"""

import pymysql
import sys	

###############################################################################
# load DATABASE SETTINGS from local file (not on git)
def grabDatabaseSettingsFromCfgFile(configFileName ="app/settings/development.cfg"):
    file = open(configFileName, 'r')
    content = file.read()
    file.close()

    paths = content.split("\n") #split it into lines
    for path in paths:
        p = path.split(" = ") # split it into "p[0] = p[1]" pairs
        if p[0] == 'DEBUG':
            debug = p[1]
        elif p[0] == 'DATABASE_HOST':
            host = p[1].replace('"','')
        elif p[0] == 'DATABASE_PORT':
            port = int(p[1])
        elif p[0] == 'DATABASE_USER':
            user = p[1].replace('"','')
        elif p[0] == 'DATABASE_PASSWORD':
            passwd = p[1].replace('"','')
        elif p[0] == 'DATABASE_DB':
            dbname = p[1].replace('"','')
        elif p[0] == 'LOCAL_PATH':
            localpath = p[1].replace('"','')
    return debug, host, port, user, passwd, dbname, localpath       
        
###############################################################################
# Establish and return MySQL database connection
def conDB(host,dbname,passwd='',port=3306, user='root'):
    try:
        con = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset='utf8')
        print("Opened database " + dbname)
    
    except pymysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    return con


###############################################################################
# return DB cursor
def curDB(conn):
 	return conn.cursor()
	
###############################################################################
# close the database
def closeDB(conn):
	curDB(conn).close()
	conn.commit()
	conn.close()
	print "Closed database " + conn.db