#from dotenv import load_dotenv
#import os

#load_dotenv()

#user = os.environ["MYSQL_USER"]
#password = os.environ["MYSQL_PASSbbWORD"]
#host = os.environ["MYSQL_HOST"]
#database = os.environ["MYSQL_DATABASE"]

DATABASE_CONNECTION_URI = f'mysql+pymysql://admin:76668813g@contactsdb.cbu56rel5olk.us-east-1.rds.amazonaws.com/contactsdb'
print(DATABASE_CONNECTION_URI)
# DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}/{database}'
# print(DATABASE_CONNECTION_URI)

