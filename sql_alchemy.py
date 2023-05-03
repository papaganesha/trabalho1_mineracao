# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'mineracao'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_engine():
        try:
            # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
            engine = create_engine(url=F"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
            return engine
        
        except Exception as ex:
            print("Connection could not be made due to the following error: \n", ex)