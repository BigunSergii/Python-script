# coding: CP1251
import codecs
import csv
import random
import sys


def phoneGen():
    listPhone = ["093", "097", "067", "050"]
    genPhone = listPhone[random.randrange(0, len(listPhone))]
    numb = ''.join(random.choice('0123456789') for _ in range(7))
    return "{0}{1}".format(genPhone, numb)


def MailGen():
    listMail = ["@gmail.com", "@ukr.net", "@hotmail.com",
                "@Outlook.com", "@i.ua", "@rambler.ru"]
    genmail = listMail[random.randrange(0, len(listMail))]
    listWord = ''.join(random.choice(
        "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZz") for _ in range(5))
    num = ''.join(random.choice('0123456789') for _ in range(3))
    return "{0}{1}{2}".format(listWord, num, genmail)


def ageGen():
    ageOfpeople = random.randrange(20, 80)
    return ageOfpeople


def genSalary():
    salaryofpeople = random.randrange(8000, 25000)
    return salaryofpeople


def mainGen(pathTofile, newfile):
    listmap = []
    with codecs.open(pathTofile, 'r', encoding='CP1251') as f:
        buff = f.readlines()
    for i in buff:
        list1 = i.split(";")
        id = list1[0]
        fullName = list1[1].split(" ")
        lastName = fullName[0]
        name = fullName[1]
        fatherName = fullName[2].strip()
        phone = phoneGen()
        mail = MailGen()
        age = ageGen()
        salary = genSalary()
        data = '{0} {1} {2} {3} {4} {5} {6} {7}\n'.format(
            id, name, lastName, fatherName, mail, age, phone, salary)
        data = data.replace(" ", ",")
        listmap.append({
            'ID': id,
            'NAME': name,
            'LASTNAME': lastName,
            'FATHERNAME': fatherName,
            'EMAIL': mail,
            'AGE': age,
            'PHONE': phone,
            'SALARY': salary
        })
        with open(newfile, 'a') as f:
            for i in data:
                f.write(i)
    return listmap
