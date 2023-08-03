import os
from dotenv import load_dotenv
from read_data import read_data_from_mysql

load_dotenv()
host_env = os.getenv("host") 
user_env = os.getenv("user") 
password_env = os.getenv("password") 
database_env = os.getenv("database") 

def main():
    read_data_from_mysql()

if __name__ == "__main__":
    main()