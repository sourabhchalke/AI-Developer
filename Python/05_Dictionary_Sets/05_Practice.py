#Practice

#Q.1 Write a program to create a dictionary of Marathi words with values as their English translatio. Provide user with an option to look it up
dic_Marathi_Words={
    "Kay":"What",
    "Kute":"Where",
    "Kon":"Who",
    "Tu":"You",
    "Kasa":"How",
    "Kadhi":"When"
}
print(dic_Marathi_Words)
searchWord=input("Enter Marathi Words : ")
print(dic_Marathi_Words.get(searchWord))

#Q.2 Write a program to input eight numbers from the user and display all the unique numbers once

num1=input("Enter 1st number : ")
num2=input("Enter 2nd number : ")
num3=input("Enter 3rd number : ")
num4=input("Enter 4th number : ")
num5=input("Enter 5th number : ")
num6=input("Enter 6th number : ")
num7=input("Enter 7th number : ")
num8=input("Enter 8th number : ")

setsOfUniqueValues={num1,num2,num3,num4,num5,num6,num7,num8}
print(setsOfUniqueValues)

#Q.3 Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

newDic={}

frd1name=input("Enter 1st friend name :")
frd1FavLanguage=input("Enter 1st friend favorite language")
frd2name=input("Enter 2nd friend name :")
frd2FavLanguage=input("Enter 2d friend favorite language")
frd3name=input("Enter 3rd friend name :")
frd3FavLanguage=input("Enter 3rd friend favorite language")
frd4name=input("Enter 4th friend name :")
frd4FavLanguage=input("Enter 4th friend favorite language")

newDic.update({
    frd1name:frd1FavLanguage,
    frd2name:frd2FavLanguage,
    frd3name:frd3FavLanguage,
    frd4name:frd4FavLanguage
})

print(newDic)

