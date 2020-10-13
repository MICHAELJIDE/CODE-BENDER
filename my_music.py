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
    
    
