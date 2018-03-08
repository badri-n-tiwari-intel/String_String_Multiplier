# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 19:00:37 2018

@author: BadriTiwari
"""

String_Num1 = "12312387859090323451234512345123"
String_Num2 = "189898909090123123453456789"


def Char_Multilier(ch1,ch2):
    num1 = int(ch1)
    num2 = int(ch2)
    Mult = num1*num2
    return Mult

def Char_Adder(InList):
    FinalList = []
    Carry= 0
    print('\n Starting List-Elementwise addition; RIGHT TO LEFT ....')
    print('\n Input List, InList = ', InList)
    for i in range(len(InList)-1, -1, -1):
        item = int(InList[i]) + Carry
        item_list = list(str(item))
        item_length = len(item_list)
        if item_length == 2:            
            Carry = int(item_list[0])
            FinalList.insert(0, int(item_list[1]))
        else:
            Carry = 0
            FinalList.insert(0, int(item_list[0]))
    if Carry > 0:
        FinalList.insert(0, int(Carry)) # Insert the Last NON ZERO Carry for the higest bit (leftmost)
        
    print('\n Output List, FinalList = ', FinalList)        
    return FinalList

def Str_Adder(Str1, Str2):
    print('\n ...........Starting function Str_Adder(Str1, Str2) ..............')
    StrPrev = Str1
    StrNew  = Char_Adder(Str2)        
    print('\n StrPrev = ', StrPrev)
    print('\n StrNew  = ', StrNew)
    Length_Prev = len(StrPrev)    
    Length_New  = len(StrNew)
    print('\n Length_Prev = ', Length_Prev)
    print('\n Length_New  = ', Length_New)
    Added_String = []
    Added_Final_String = []
    
    if Length_New > Length_Prev:
        print('String Lengths are NOT SAME: Length_New > Length_Prev. (Length_New - Length_Prev) = ', (Length_New - Length_Prev))
        # prepend zeros
        for num in range(Length_New - Length_Prev):
            StrPrev.insert(0, 0)
            
    elif Length_New < Length_Prev:
        print('String Lengths are NOT SAME: Length_New < Length_Prev. Length_Prev - Length_New = ', (Length_Prev - Length_New))
        #prepend zeros        
        for num in range(Length_Prev - Length_New):
            StrNew.insert(0, 0)
    
    if len(StrNew) == len(StrPrev):
        print('String Lengths are SAME. \n Starting the charwise Addition......')
        print('\n StrPrev = ', StrPrev)
        print('\n StrNew  = ', StrNew)
        for index in range(len(StrNew)):
            #print('\n Adding int(StrPrev[index]) = ', int(StrPrev[index]), ' AND int(StrNew[index]) =', int(StrNew[index]))
            Added_String.append(int(StrPrev[index]) + int(StrNew[index])) 
        
        print('\n Added_String  = ', Added_String)
    else:
        print('String Lengths are Still NOT THE SAME')
    
    Added_Final_String = Char_Adder(Added_String)   
    print('\n Added_Final_String  = ', Added_Final_String)
    print('\n **************Finishing function Str_Adder(Str1, Str2) *****************')
    return Added_Final_String
    
def Str_Multiplier(String_Num1, String_Num2):
    s1 = String_Num1
    s2 = String_Num2
    IndividualProducts = []    
    AllProducts = []
    Counter = 0
    for i in range(len(s2), 0, -1):
        IndividualProducts = []
        for j in range(len(s1), 0, -1):
            print('\n char1 = ', s2[i-1], 'char2 = ', s1[j-1] )
            result1 = Char_Multilier(s2[i-1],s1[j-1])            
            #IndividualProducts.append(result1)
            IndividualProducts.insert(0, result1)
            print('\n result1 = ', result1)
            print('\n IndividualProducts = ', IndividualProducts)
        
        print('Counter (number of Zeros to Append) = ', Counter)
        for count in range(Counter):            
            IndividualProducts.append(0)
            print('Appended a ZERO....')
        Counter +=1    
        AllProducts = list(map(int, AllProducts))
        print('\n StrPrev = ', AllProducts)
        print('\n StrNew  = ', IndividualProducts)
        AllProducts = Str_Adder(AllProducts, IndividualProducts)
    return AllProducts

Result_List = Str_Multiplier(String_Num1,String_Num2)
Result_String = ''.join(str(character) for character in Result_List)
#Result.reverse()
print('\n Multiplication of String1 = ', String_Num1, ', and, String2 = ', String_Num2)
print('\n Regular multiplication int(s1)*int(s2) = ', int(String_Num1)*int(String_Num2))
print('\n Single-Digit Char muliplication, Result_List = ', Result_List)
print('\n Single-Digit Char muliplication, Result_String = ', Result_String)