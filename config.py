from dotenv import load_dotenv
import os

load_dotenv()

us = os.environ['DB_USER']
pasw = os.environ['DB_PASSWORD']
db_data = os.environ['DB_DATABASE'] 

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{us}:{pasw}@localhost/{db_data}'
