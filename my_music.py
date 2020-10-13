# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 08:32:42 2020

@author: lenovo
"""


'''my_music is about my best song and its attributes, this function is
 to be able to call any of the 3 attributes'''
 
def my_music(Genre, Artist, Year):
    
     print({Genre})
     
     print({Artist})
     
     print({Year})
     
     print(f"\nMy music type is {Genre}. ")
     
     print(f"\nMy music author is {Artist}. ")
     
     print(f"\nyear of publishing is {Year}. ")
    
     
     
my_music('Afrobeats', 'Mr_Eazy', 2019)





'''calling each of the songs three attributes Artist, Genre
 and year as individual function.'''
 

def my_Artist (Artist):
    
    print(Artist)
    
    print("The song author is " + Artist)
    
    
my_Artist("Mr_Eazy")


def my_Genre (Genre):
    
    print(Genre)
    print("The type of my best song is " + Genre)
    
    
my_Genre("Afrobeats")



def Song_year(Year):
    
    print(Year)
    print("My best song was published in the year " + "2019")
    
Song_year(2019)




# TO CONFIRM THE GENRE WITH A BOOLEAN IF GENRE = Afrobeats

#def my_Genre():
    
    #return True

#if my_Genre():
    
    #print("YES!")
#else:
    #print("NO")
    


def my_Genre(Afrobeats):
    
    return True

if my_Genre("Afrobeats"):
    print("YES!")
else:
    print("NO")
    
    
def printmessage(message, ntimes=1):
      print(message * ntimes)

printmessage("Hello")
printmessage("Hello", 5)




def sumA(count):
    a = count+1
    return a 
    print(a)
 
    
    
sumA(3)

print (sumA(3))


def sumA(count):
    a = count+1
    return a 
    print(a)
 
    
    
sumA(6)

print (sumA(6))



num =1

def func():
    num = 4
    print(num)
    
func()
print(num)
         
         


Temperature = 20
Thermo = 15
if Temperature < 15:
    Thermo = Thermo + 5
    
print(Thermo)




def max(a,b):
    if a>b:
        print('a is the max')
    else:
        print('b is the max')
    
max(1,2)


if (10<0) and (0<-10):
    print ("A")
    
else:
    print("B")
    

a = "b"

if True or True:
    
    a = "a"
    
print(a * 2)    
 


Temperature = 20
Thermo = 15
if Temperature < 15:
    Thermo = Thermo + 5
    
print(Thermo)
    


Time = "Day"
Sleepy = False
Pajamas = "Off"

if Time == "Night" and Sleepy == True:
    Pajamas = "On"
    
print(Pajamas)


if (10<0) and (0<-10):
    print ("A")
    
else:
    print("B")
    
    
a = "b"

if True or True:
    
    a = "a"
    
print(a * 2)    
     

if (10<0) and (0<-10):
    print ("A")
    
else:
    print("B")
    
    
    
    
#a = 20
#b = 30
#c = 25

#nums = [20,30,25]

#for numbers in nums:
    #if nums == 20:
        #print(True)
    #else:
        #print(False)

#for numbers in nums:
    
        
    #if nums == 30:
       #print(True)
    #else:
        #print(False)
        
        
#for numbers in nums:
    #if nums ==  25:
        
        #print(False)
    #else:
        #print(True)
        
        
x = 20
y = 25
z = 30

if x == y or x == z :
    
    print(True)
else:
    print(False)
    

a = 4
b = 6
c = "8"

if a == b or c == a :    
    print (False)
else:
    print(True)
    
    
    
    
    
    
    
li = [['john','doe']]

print(li[-1][-1])


#myUniqueList()

def myUniqueList(food):
    for x in food:
        print(x)
        
fruits = ["mango","tangerine","pear"]

#myUniqueList(fruits)

cereals = ["maize","rice","wheat"]

vegetables = ["spinach","broccoli","carbage"]


myUniqueList(fruits)

myUniqueList(cereals)

myUniqueList(vegetables)
    
myUniqueList = ["mango","tangerine","pear","maize",
                      "rice","wheat","spinach","broccoli","carbage"]

print(myUniqueList)