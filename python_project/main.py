from dataGen import *
from funcDB import *
import argparse
import os

parser = argparse.ArgumentParser(description=('''
Generated parametrs as: mail, age, phone, salary and add them to file after add them to database.
python3 main.py --instal-mysql (install mysql on ubuntu server)
python3 main.py --create-dataBase --create-table (create database and table)
python3 main.py --dataBaseName --tableName (database name and table name to use)
python3 main.py --fileSchema (file Schema)
python3 main.py --migration --people-list --people-outlist (use file with people list and generate parametrs to them then append them to output file and make to migration in database)
python3 main.py --ip-addres --username --password (ip address, username and password to connect in database)
'''))
parser.add_argument('--install-mysql', dest="installMysql", default=None, type=str, help="install-mysql", required=False)
parser.add_argument('--create-dataBase', dest="crateDataBase", default=None, type=str, help="create data base", required=False)
parser.add_argument('--create-table', dest="createTable", default=None, type=str, help="create data table", required=False)
parser.add_argument('--dataBaseName', dest="dataBaseName", type=str, help="Name of data base to use", required=True)
parser.add_argument('--tableName', dest="tableName", type=str, help="Name of table to use", required=True)
parser.add_argument('--fileSchema', dest="fileSchema", default=None, type=str, help="fileSchema", required=False)
parser.add_argument('--migration', dest="migrationOfDatabase", default=None, type=str, help="migration to data base", required=False)
parser.add_argument('--people-list', dest="peopleList", type=str, help="path to file with people list", required=False)
parser.add_argument('--people-outlist', dest="peopleOuthList", type=str, help="path to file with generate of people list", required=False)
parser.add_argument('--ip-addres', dest="ipAddress", default=None, type=str, help="ip to remote mySql", required=False)
parser.add_argument('--username', dest="userName", default=None, type=str, help="name of user to mySql", required=False)
parser.add_argument('--password', dest="password", default=None, type=str, help="password of user to mySql", required=False)
args = parser.parse_args()
installSql = args.installMysql
crateDB = args.crateDataBase
crateTable = args.crateDataBase
dbName = args.dataBaseName
tableName = args.tableName
schema = args.fileSchema
migration = args.migrationOfDatabase
peopleList = args.peopleList
peopleOutList = args.peopleOuthList
ip = args.ipAddress
user = args.userName
passwd = args.password

def main():
    if migration != None and ip != None and user != None and passwd != None:
        Data = dataGen.mainGen(peopleList, peopleOutList)
        #print("we are in main")
        print(Data)
        migrationDB.mainMigration(ip, dbName, tableName, user, passwd, Data)
    if  dbName != None and tableName !=None and ip != None and user != None and passwd != None:
        migrationDB.mainCreate(dbName, tableName, user, passwd, ip)
    if installSql = "yes":
        #instMysql = 'apt install mysql-server'
        statusMysql = 'systmctl status mysql'
        os.system(statusMysql)

main()

