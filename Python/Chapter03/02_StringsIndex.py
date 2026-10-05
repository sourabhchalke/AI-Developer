#Indexing
name = "Sourabh Chalke"
print(len(name))

print("2nd Index value of name is :",name[2]) #Indexing starts from 0(Zero) from beginning of String
print("-4 Index value of name is :",name[-4]) #Indexing starts from -1(minus one) from end of String

print("Slice Method :",name[0:4]) #Slice Method:- Return 0 to 3 index values and exclude 4

print("Negative Slice Method :",name[-9: -2])

print("Colon Four(:4) value is :-",name[:4]) #[:4] means [0:4]
print("Five Colon(5:) value is :-",name[5:]) #[5:] means [5:length of string]

#Slicing with skip value
print("Slicing with skip value :",name[2: 8: 3])
