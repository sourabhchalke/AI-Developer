#Method	Use	Example
#lower()	        lowercase	                  s.lower()
#upper()	        uppercase	                  s.upper()
#strip()	        remove spaces	              s.strip()
#replace()	        replace text	              s.replace("Python", "World")
#split()	        string → list	              "a,b,c".split(",")
#join()	            list → string	              ",".join(["a","b","c"])
#find()	            find position	              s.find("Python")
#count()	        count occurrences	          s.count("o")
#startswith()	    check beginning	              s.startswith("Hello")
#endswith()	        check ending	              s.endswith("Python")
#isdigit()	        check digits	              "123".isdigit()
#isalpha()	        check letters	              "abc".isalpha()
#isalnum()	        letters/numbers	              "abc123".isalnum()

name = " sourabh chalkE"                  
name2="Python"

print("Lower Method :-",name.lower()) #Convert string into lowercase
print("Upper Method :-",name.upper()) #Convert string into uppercase
print("Strip Method :-",name.strip()) #Return a copy of the string with leading and trailing whitespace removed
print("Replace Method :-",name.replace("sourabh","Akash")) #Return a copy with all occurrences of substring old replaced by new
print("Split Method :-",name.split()) #Return a list of the substrings in the string, using sep as the separator string.
print("Join Method :-",name.join(name2)) #The string whose method is called is inserted in between each given string. The result is returned as a new string
print("Find Method :-",name.find("a")) #Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]
print("Count Method :-",name.count("h")) #count occurrences
print("Startswith Method :-",name.startswith(" so")) #Return True if the string starts with the specified prefix, False otherwise.
print("Endswith Method :-",name.endswith("bh")) #Return True if the string ends with the specified suffix, False otherwise.
print("Isdigit Method :-",name.isdigit()) #Return True if the string is a digit string, False otherwise.
print("Isalpha Method :-",name.isalpha())
print("Isalnum Method :-",name.isalnum())





