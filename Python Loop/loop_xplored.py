# s = 'F','A','R','D','I','N'
# sp =""
#
# for i in s:
#   sp = i+sp
#   print(sp[::-1],end=)
import random

#For Loop in a list

# pro =[1,2,3,4,5,6,7,8,9]
# avg =0
# for i in pro:
#     avg = avg + i
# print("Sum of Total No in list : ",avg)
# print('Average : ',avg/len(pro))

#For Loop in a tuple
# num = (10,20,60,90)
# sum = 0;
# for i in num:
#     sum = sum+i
#     print(sum)

# range function
# sum =0
# for i in range(1,2):
#    sum = sum+i
#    print(sum)

# Print Multiplication Table

# n = int(input("Enter Number of :"))
# for i in range(1,11):
#     print(f" {n} * {i} = {n*i}")

#
# list = ['Fardin','Ahosan','Miao']
# for i in list:
#     print(i)


#matrix multiplication

# a=[1,2,3,4,5,6,7,8,9]
# b=[9,8,7,6,5,4,3,2,1]
# for i in range(len(a)):
#     for j in range(len(b)):
#         print(f" {a[i]} * {b[j]} = {a[i] * b[j]}")

# companies = ['Google','Amazon','Meta']
# for i in range(len(companies)):
#     print(companies[i])
#     for j in companies[i]:
#         print(j)



# for i in range(1,100,30):
#     print("Miao")
# else:
#     print("Printed Done")

# #Break/Continue
# miao = 100
# lop =[56,33,56]
# for i in range(1,200):
#     if i in lop:
#         print('Skipped--:',i)
#         continue
#     print(f'Printed till ',i)

# # Total Gaol has player scored
# player_name  = input("Enter Player Name: ")
# player_list = {'Ahosan': 190, 'Fardin': 459,'Poland':900}
#
# for i in player_list:
#     if i == player_name:
#         print(f"{i} has scored {player_list[i]} goals in this season,Cheers")
#         break
# else:
#     print('No Player in this data')


# data =[1,6,4,35,7,2,67,7]
# cube=[]
# for i in data:
#     cube.append(i*100)
#     print(cube)
#


#Pattern Printing------------------------------------------------
# a =["+","*","/","-"]
# dis =random.choice(a)

""" 
----Star Printing-------------
* 
* * 
* * * 
* * * * 
* * * * * 
"""

# for i in range(5):
#     for j in range(i+1):
#         print(dis,end=" ")
#     print()
#

""" 
----Star Printing-------------

* * * * * 
* * * * 
* * * 
* * 
* 

"""

# for i in range(5):
#     for j in range(5-i):
#         print(dis, end=" ")
#     print()





"""
* * * * * * * * * * 
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 

"""

# for i in range(10):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# #
# for k in range(10):
#     for l in range(k+1):
#         print("*",end=" ")
#     print()





"""

Hill  Pattern
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 



"""

#
# n=5
#
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()





"""

 Reverse Hill  Pattern
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 



"""
#
# n=5
# for i in range(5):
#     for j in range(i+1):
#         print(" ",end=" ")
#
#     for j in range(i,n):
#         print("*",end=" ")
#
#     for  j in range(i,n-1):
#         print("*",end=" ")
#     print()



"""
######Diamond Shape
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 

"""
######Diamond Shape
#
# for i in range(4):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# for i in  range(5):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,5):
#         print("*",end=" ")
#     for j in range(i,5-1):
#         print("*",end=" ")
#     print()
#
#


##Pyramid
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

##Right Trinagle

# n=5
# for  i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

##Left Triangle

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

## R. Downward Trinagle

#n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

## L. Downward Triangle

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(" ",end="*")
#     print()

# ##Double Hill
# n=5
# for i in range(5):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#
#     print()

