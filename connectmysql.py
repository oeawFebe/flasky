# https://pypi.org/project/python-dotenv/
import mysql.connector
from dotenv import dotenv_values


def get_block():
    return ("0000", "00000000")


config = dotenv_values(".env")
pwd = config["MYSQL_PASSWORD"]
# connecting to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pwd,
    database="bitnami_wordpress"
)
mycursor = mydb.cursor()


sql = "INSERT INTO aristophanes (blocknumber, amount) VALUES (%s, %s)"
val = [
    get_block(),  # ("INT", "BITINT")
]
mycursor.executemany(sql, val)

mydb.commit()
