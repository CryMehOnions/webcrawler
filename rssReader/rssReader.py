import psycopg2

try:
	conn = psycopg2.connect("dbname='mmda_traffic' user='direksyon' host='localhost' password='gothere4lyf'")
except:
	print "Cannot connect to database"