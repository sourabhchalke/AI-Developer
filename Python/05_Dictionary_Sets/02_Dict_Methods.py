#Dictionary Methods

marks = {
    "Chinmay":95,
    "Akash":92,
    "Abhijit":74,
    "Rohit":84
}

print(marks["Akash"]) #If key not found then it throw error
print(marks.get("Akash")) #If key not found then it return none

print(marks.items())

print(marks.keys())
print(marks.values())
marks.update({"Chinmay":76})
print(marks)

print(marks.__sizeof__())