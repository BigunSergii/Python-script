# coding: CP1251
import random 
import string
import codecs
from random import randint      
#---------------------Random Phone---------------------
def random_phonenumber():
   phonelist = ["093","068","097","067"]
   numb = ''.join(random.choice('0123456789') for _ in range(7))
   return "{0}{1}".format(phonelist[random.randrange(0,len(phonelist))],numb) 
  

#---------------------Random Mail----------------------
def random_mailchar(y):
      return ''.join(random.choice(string.ascii_letters) for x in range(y))
 
#---------------------Random Age----------------------
def random_age():
    number = random.randrange(18,99) 
    return number

#---------------------Random Sallery----------------------
def random_sallery():
    numbers = random.randrange(10000,100000) 
    return numbers


def mainGen(pathTofile, newfile):
    peoplemas = []
    with codecs.open(pathTofile, 'r', encoding='CP1251') as f:
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
        data = '{0} {1} {2} {3} {4} {5} {6} {7}\n'.format(id,name,lastName,fatherName,mail,age,phone,salary)
        data = data.replace(" ",",")
        with open(newfile, 'a') as f:
            for i in data:
                f.write(i)
    return peoplemas
        

# newfile = "C:/Users/alexj/Desktop/projectPython/newpeople.csv"
# pathTofile = "C:/Users/alexj/Desktop/projectPython/people.csv"
# mainGen(pathTofile, newfile)
# print("ID:{0}|Name:{1}|Surname:{2}|Fathername:{3}|Mail:{4}|Age:{5}|Phone:{6}|Wage:{7}\n".format(i['ID'],i['NAME'],i['LASTNAME'],i['FATHERNAME'],i['EMAIL'],i['AGE'],i['PHONE'],i['SALARY']))

# def readfile(newfile):
#     with open(newfile, 'r') as f1:
#        buff = f1.readlines()
#        print(type(buff))
#        for i in buff:
#            print(i)

# readfile(newfile)





