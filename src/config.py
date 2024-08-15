from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")
port = os.getenv("MYSQL_PORT", 3306)  # Valor por defecto 3306 si no se especifica

DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
# from dotenv import load_dotenv
# import os

# load_dotenv()

# user = os.environ["MYSQL_USER"]
# password = os.environ["MYSQL_PASSWORD"]
# host = os.environ["MYSQL_HOST"]
# database = os.environ["MYSQL_DATABASE"]


# DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}/{database}'
#print(DATABASE_CONNECTION_URI)