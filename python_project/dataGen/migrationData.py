import mysql.connector
def migrationDB (migrationData):
    # mydb = mysql.connector.connect(
    # host="localhost",
    # user="serhii",
    # passwd="1234",
    # database="testDB"
    # )
    for i in migrationData:
        print(i)





# mydb = mysql.connector.connect(
#   host="localhost",
#   user="serhii",
#   passwd="1234",
#   database="testDB"
# )
# mycursor = mydb.cursor()
# print(mydb)
# sql = "INSERT INTO people (ID, NAME, LASTNAME, FATHERNAME, EMAIL, AGE, PHONE, SALARY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# pathTofile = "/home/serhii/Scripts/python_project/dataGen/generatedPeople.csv"
# #pathTofile = "/home/serhii/Scripts/python_project/testpeople.txt"
# listmap = []
# with open(pathTofile, 'r') as f:
#     buff = f.readlines()
# for i in buff:
#     list1 = i.split(",")
#     id = list1[0]
#     name = list1[1]
#     lastName = list1[2]
#     fatherName = list1[3]
#     phone = list1[6]
#     mail = list1[4]
#     age = list1[5]
#     salary = list1[7]
#     data = '{0} {1} {2} {3} {4} {5} {6} {7}\n'.format(id,name,lastName,fatherName,mail,age,phone,salary)
#     data = data.replace(" ",",")
#     listmap.append({
#         'ID': id,
#         'NAME': name,
#         'LASTNAME': lastName,
#         'FATERNAME': fatherName,
#         'EMAIL': mail,
#         'AGE': age,
#         'PHONE': phone,
#         'SALARY': salary
#     })
#     #print(list1)
#     val = [list1]
#     mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")