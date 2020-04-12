from .dataGen
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="cerber",
    passwd="cerber",
    database="itstep"
)
mycursor = mydb.cursor()
print (mydb)
sql = "INSERT INTO people (ID, NAME, LASTNAME, FATHERNAME, EMAIL, AGE, PHONE, SALARY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
pathTofile = "/home/projectPython/dataGen/people.csv"
listmap = []
with open(pathTofile, 'r') as f:
    buff = f.readlines()
for i in buff:
        list1 = i.split(";")
        id = list1[0]
        fullName = list1[1].split(" ")
        name = fullName[0]
        lastName = fullName[1]
        fatherName = fullName[2].strip()
        phone = random_phonenumber()
        mail = random_mailchar(7)+"@gmail.com"
        age = random_age()
        salary = random_sallery()
        data = '{0} {1} {2} {3} {4} {5} {6} {7}\n'.format(id,name,lastName,fatherName,mail,age,phone,salary)
        data = data.replace(" ",",")
        peoplemas.append({
            'ID':id,
            'NAME':name,
            'LASTNAME':lastName,
            'FATHERNAME':fatherName,
            'EMAIL':mail,
            'AGE':age,
            'PHONE':phone,
            'SALARY':salary
        })
        val = [list1]
        mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")