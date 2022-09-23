from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


db = SQLAlchemy()
engine = create_engine(f'mysql+pymysql://admin:76668813g@contactsdb.cbu56rel5olk.us-east-1.rds.amazonaws.com/contactsdb', pool_size=10, max_overflow=20)
