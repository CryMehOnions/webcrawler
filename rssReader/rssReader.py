#!/usr/bin/python

import psycopg2
import feedparser

feedURL = "http://mmdatraffic.interaksyon.com/livefeed/"
dataDict = feedparser.parse(feedURL)
entryList = []

for data in dataDict:
	title = data.title.split('-')
	entry = {'location_road' : title[0], 'location_area' : title[1], 'location_bound' : title[2], 'traffic' : data.description, 'guid' : int(data.guid), 'update_timestamp' : data.pubDate}
	entryList.append(entry)

try:
	conn = psycopg2.connect("dbname='mmda_traffic' user='direksyon' host='localhost' password='gothere4lyf'")
	print "Connection Successful"

	insertQuery = """INSERT INTO entries (location_road, location_area, location_bound, traffic, guid, timestamp) VALUES (%(location_road)s, %(location_area)s, %(location_bound)s, %(traffic)s, %(guid)i, %(timestamp)s)"""

	cur = conn.cursor()

	cur.executemany(insertQuery, tuple(entryDict))

	conn.close()
except:
	print "Cannot connect to database"

