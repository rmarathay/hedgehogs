# * ProvisionSchema initializes the database for Scraper and creates the appropriate schema
import psycopg2
import sys

def connectDB(secret):
	"""connectDB() attempts to create a connection with the database
    Args:
        secret: The password used to authenticate
    Returns:
        A new connection object (to the PostgreSQL server)
    """
	try:
		conn = psycopg2.connect(host="206.189.181.163", dbname="rcos", user="rcos", password=secret)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return conn

def closeDB(conn):
	"""closeDB() attempts to close the connection (make it unusable)
    Args:
        conn: The connection object that is closed
    """
	print("Attempting to close connection with database")
	if (conn!=None):
		print("Connection successfully closed")
		conn.close()

	else:
		print("Database connection already closed")

# def verifyTableName(cursor,tableName):
# 	"""verifyTableName checks that a table with the name doesn't already exist
#     Args:
#         cursor: The cursor to the current database session
#         tableName: The string representing the table name
#     Returns:
#         table name if an existing table with that name does not exist
#     """
# 	cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")	
# 	if tableName in cursor.fetchAll():
# 		raise Exception ("Table with name " + tableName + " already exists!")
# 	else:
# 		return tableName

def createSchema(conn, cursor, companyName):
	"""createSchema creates the schema and creates a table for each company
	Args:
		cursor: The cursor to the current database session
        conn: The connection object to the current database session
        companyName: list of company names
	"""
	sql = "CREATE SCHEMA stockData AUTHORIZATION rcos"
	try:
		cursor.execute(sql)
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	for i in range(0, len(companyName)):
		createTable = "CREATE TABLE IF NOT EXISTS stockData.{} (    \
				open            float(4),   \
				high            float(4),   \
				low             float(4),   \
				close           float(4),   \
				volume          int \
				);".format(tableName[i])
		try:
			cursor.execute(createTable)
			conn.commit()
		except Exception as e:
			print(e)
			conn.rollback()



def restartDB(conn):
	"""restartDB() restarts the database connection
    Args:
        conn: The connection object that is closed
    Returns:
        A new connection object to the PostgreSQL database
    """
	print("Beginning connection restart")
	closeDB(conn)
	conn = connectDB()
	print("Finished connection restart")
	return conn

def prepDB(conn, cursor, tableName):
	"""prepDB() creates the schema for the data
    Args:
        conn: The connection object to the current database session
        cursor: The cursor to run database commands on the current session
        tableName: The desired table name for the specific stock data
    Returns:
        A new connection object to the PostgreSQL database
    """
	try:
		cursor.execute("CREATE TABLE {} (    \
				open            float(4),   \
				high            float(4),   \
				low             float(4),   \
				close           float(4),   \
				volume          int \
				);".format(tableName))
		conn.commit()
		conn.close()
	except Exception as error:
		print(error)
		conn.rollback()
		closeDB(conn)

def main():
	if (len(sys.argv)<3):
		sys.exit("Must provide at least one table name")
	conn = connectDB(sys.argv[1])
	cursor = conn.cursor()
	for i in range(2, len(sys.argv)):
		tableName = sys.argv[i]
		prepDB(conn, cursor, tableName)

if __name__ == '__main__':
	main()

