#1
list1= ['hello', 1, True]
x=input('1: ')
y=input('2: ')
print(list1)
list1.append(x)
list1.append(y)
print(list1)


#2
list1= ['hello', 1, True]
x=input('1: ')
y=input('2: ')
newlist=list1.copy()
newlist.append(x)
newlist.append(y)
print(list1)
print(newlist)


#3
list2=[1,2,3,4,4,4,5]

x=int(input('Check (x): '))
      
print('number of x: ',list2.count(x))



#4
list4=[1,2,3,4,4,4,5]

print("before: ",list4)
x=int(input('X: '))
listn=list4.copy()
listn.remove(x)
print("after: ",listn)



#5
list5=[1,2,3,4,5,6,7]
list5.pop(5)
list5.pop(4)
list5.pop(0)
print(list5)


#6
list5=[1,2,3,4,5,6,7]
listnew=list5.copy()
listnew.pop(5)
listnew.pop(4)
listnew.pop(0)
print(list5)
print(listnew)



#7
l1=[1,2,3,4,5]
print(l1)
l2=['a','b','c']
print(l2)
l1.pop(-1)
l1.append(l2)
print(l1)



#8
set1={1,2,3,4,5,6}
x=set([int(input('New element: '))])     
set1.union(x)


#9
set2 =  {False,1,'hello', 'barev'}
print(set2)
set2.remove(input('check: '))
print(set2)



#10
set2 =  {False,1,'hello', 'barev'}
print(set2)
set2.discard(input('check: '))
print(set2)


#11
set1={1,2,3}
set2={2,3,4}
print('\n', set1,'\n',set2,'\n',set1.union(set2),'\n',set1.intersection(set2))



#12
set3={1, 2, 3, 4, 5, 6, 8}
print('min: ',min(set3))
print('max: ',max(set3))
min(set3)<int(input('Check: '))<max(set3)



#13
t1 = (1, 2, 3, 4, 5, 6, 7 )
print(t1[3])
print(t1[-4])



#14
t2 = (1, 2, 3, 4, 5, 6, 7 )
print(t2)
t2=list(t2)
t2[3]='hello'
print(tuple(t2))



#15
dict1={'a': 1, 'b': 2, 'c': 3, 'd': 4}
#dict1[input('key: ')]=int(input('value: '))
x=input('key: ')
y=input('value: ')
dict1[x]=y
print(dict1)



#16
l1= [(1, 'a'), (2,'b'), (3,'c')]
dict1={l1[0][0]:l1[0][1],l1[1][0]:l1[1][1],l1[2][0]:l1[2][1]}
print(dict1)