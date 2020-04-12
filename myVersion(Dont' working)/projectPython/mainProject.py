from dataGen import *
import argparse

parser = argparse.ArgumentParser(description='Parser to mogration people list to data base')
parser.add_argument('--install-mysql', dest="installMysql", default=None, type=str, help="install-mysql", required=False)
parser.add_argument('--create-dataBase', dest="crateDataBase", default=None, type=str, help="create data base", required=False)
parser.add_argument('--create-table', dest="createTable", default=None, type=str, help="create data table", required=False)
parser.add_argument('--dataBaseName', dest="dataBaseName", type=str, help="Name of data base to use", required=True)
parser.add_argument('--tableName', dest="tableName", type=str, help="Name of table to use", required=True)
parser.add_argument('--fileSchema', dest="fileSchema", default=None, type=str, help="fileSchema", required=False)
parser.add_argument('--migration', dest="migrationOfDatabase", default=None, type=str, help="migration to data base", required=False)
parser.add_argument('--people-list', dest="peopleList", type=str, help="path to file with people list", required=True)
parser.add_argument('--people-outlist', dest="peopleOuthList", type=str, help="path to file with generate of people list", required=True)
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

def main():
    if migration != None and ip != None and user != None and passwd != None:
        migrationdata = dataGen.mainGen(peopleList, peopleOutList)
        migrtation(ip, dbName, tableName, user, passwd, migrationdata)



a = dataGen.mainGen("C:/Users/alexj/Desktop/projectPython/dataGen/people.csv","C:/Users/alexj/Desktop/projectPython/dataGen/newpeople.csv")
print(a)
# for i in a:
#     print("ID:{0} Name:{1} Surname:{2} Fathername:{3} Mail:{4} Age:{5} Phone:{6} Wage:{7}\n".format(i['ID'],i['NAME'],i['LASTNAME'],i['FATHERNAME'],i['EMAIL'],i['AGE'],i['PHONE'],i['SALARY']))
