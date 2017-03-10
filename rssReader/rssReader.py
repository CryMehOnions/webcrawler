#!/usr/bin/python

import psycopg2

try:
	conn = psycopg2.connect("dbname='mmda_traffic' user='direksyon' host='localhost' password='gothere4lyf'")
	print "Connection Successful"
except:
	print "Cannot connect to database"

cur = conn.cursor()
