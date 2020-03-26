#Problem 1
name=input('Name: ')
last_name=input('Last name: ')


#Problem 2
num1=int(input('num1: '))
num2=int(input('num2: '))
SUM=num1+num2
print(SUM)


#Problem 3
age=int(input('age: '))
print('Happy Birthday, you are already %d years old!'% age)


#Problem 4
text=input("Type your text: ")
print(text.upper())
print(text.lower())



#Problem 5
text=input("Type your text: ")
print(text.count('a'))
print(text.count('b'))
print(text.count('c'))
print(text.count('d'))
print(text.count('e'))


#Problem 6
str1='How are you John?'
name='Rafayel'
print(str1[:12]+name+'?')
print(str1.replace("John",name))


#Problem 7
country='Armenia'
years=10
print(""""Hi, where are you from?
I’m from %s
How long have you lived here?
For %d years"""""%(country,years))


#Problem 8
#problem1
import time
import datetime
import calendar

num_y=int(input('Years:' ))*365
num_d=int(input('Days:' ))
tday = datetime.datetime.today()
tdelta=datetime.timedelta(days = num_y + num_d)
print('Current date: ',tday)hu
print('Date today + years + days: ', tday + tdelta)


#problem2
text=input("Text: ")
x=len(text)
y=x/2-1
z=x/2+2
text1=text[0:int(y)]+text[int(y):int(z)].upper()+text[int(z):]
print("Middle 3: ",text[int(y):int(z)])
print("new string: ",text1)


#problem3
text=input("Text: ")
x=input("find: ")
y=input("replacec with: ")
print(text.replace(x,y))


#problem4
text=input("Text: ")
print("The USA/usa count is: ",text.count("USA")+text.count("usa"))
s1=text.replace('USA','Armenia')
s2=s1.replace('usa','Armenia')
print('The new string: ', s2)


#problem5
bd = datetime.datetime(1992, 12, 23)
print('My Birthdate: ',bd)
print('My Birthdate year: ',bd.year)
print('My Birthdate month: ',bd.month)
print('My Birthdate day: ',bd.day)
print('My Birthdate day of the week: ',bd.isoweekday())
cal = calendar.month(2017, 5)
tday = datetime.date.today()
bday = datetime.date(2020, 12, 23)
till_bday = bday - tday
print("Days until my next birthday: ", till_bday)
print ("Here is the calendar:")
print (cal)
one_day = datetime.timedelta(days = 1)
two_days = datetime.timedelta(days = 2)
three_days = datetime.timedelta(days = 3)
yesterday=tday-one_day
print('Yesterday: ',yesterday)
print('Yesterday + 2 days: ',yesterday+two_days)
print('Yesterday - 3 days: ',yesterday-three_days)