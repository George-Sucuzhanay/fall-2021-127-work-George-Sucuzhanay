# CSV Data Project
# Author: George Sucuzhanay
# Using NYC Open Data Unbanked Dataset: 
# https://data.cityofnewyork.us/Business/Where-Are-the-Unbanked-and-Underbanked-in-New-York/v5w4-adxa

import csv

# Create a dictionary where
    # 1) Keys are the boroughs of NYC
    # 2) Values are the percentage of unbanked in such borough

# Find the borough with the most underbanked will need the mode function
    # check to see it is also the borough with the highest percantage of foreign born

# Find the borough with highest median income
    # compare it with the borough with the lowest median income
    # compare the underbanked perctanges of these 2 boroughs

    # Assumption before correlation w/ CSV:
    # small median income => greater chances of being unbanked
    # large median income => lower chances of being unbanked


f = open("data/underbanked.csv", encoding='Latin-1')
f2 = open("data/underbanked.csv", encoding='Latin-1')
f3 = open("data/underbanked.csv", encoding='Latin-1')

reader = csv.reader(f)
mydict = dict((rows[0],rows[4]) for rows in reader)

def largestUnbankedPercent():
    keyList = []
    for i in sorted (mydict.values()):
        keyList.append(str(i))
    largest = keyList[-2]
    return largest

def get_key_l_unbanked(val): 
    for key, value in mydict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

# This here lets us know the borough in NYC that has the largestUnbankedPopulation
print(get_key_l_unbanked(largestUnbankedPercent()), "is the borough with the largest population of unbanked people.")

reader2 = csv.reader(f2)
dictForeignBorn = dict((rows2[0],rows2[9]) for rows2 in reader2)
# print(dictForeignBorn)

def largestForiegnBornPercent():
    keyList = []
    for i in sorted (dictForeignBorn.values()):
        keyList.append(str(i))
    largest = keyList[-2]
    return largest

def get_key_foreign(val): 
    for key, value in dictForeignBorn.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"

print(get_key_foreign(largestForiegnBornPercent()), "has the highest population of foriegn born people.")

def corrolationForiegnUnbanked():
    if get_key_l_unbanked(largestUnbankedPercent()) == get_key_foreign(largestForiegnBornPercent()):
        return "The borough with the largest unbanked population match the borough with largest foriegn born population."
    else:
        return "The borough with the largest unbanked population does not match the borough with largest foriegn born population."
print(corrolationForiegnUnbanked())


reader3 = csv.reader(f3)
dictMedianIncome = dict((rows3[0],rows3[11]) for rows3 in reader3)
# print(dictMedianIncome)

def largestMedianIncome():
    keyList = []
    for i in sorted (dictMedianIncome.values()):
        keyList.append(str(i))
    largest = keyList[-2]
    return largest

def get_key_l_income(val): 
    for key, value in (dictMedianIncome.items()): 
         if val == value: 
             return key 
    return "key doesn't exist"

print(get_key_l_income(largestMedianIncome()))
# print(get_key_l_income(largestMedianIncome()), "is the borough with the highest median income.")

def corrLMedianUnbanked():
    if get_key_l_income(largestMedianIncome()) == get_key_l_unbanked(largestUnbankedPercent()):
        statement = print(get_key_l_income(largestMedianIncome()), "is also the largest unbanked borough")
        return statement
    else:
        statement = print(get_key_l_income(largestMedianIncome()), "and" , get_key_l_unbanked(largestUnbankedPercent()), " do not correlate at all." )
        return statement

print(corrLMedianUnbanked())

