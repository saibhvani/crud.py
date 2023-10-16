#curd operations
#create operation
#append
lst=["bhavani","chinni","sravya"]
lst.append(lst)
print(lst)

#insert
attendees =["bhavani","chinni","sravya"]
attendees.insert(2,"saibhavani")
print(attendees)

#read operation
attendees =["bhavani","chinni","sravya"]
print(attendees.count("bhavani"))

attendees =["bhavani","chinni","sravya","abc"]
print(attendees.count("abc"))

attendees =["bhavani","chinni","sravya","abc"]
print(attendees.count("abc"))

attendees =["bhavani","chinni","sravya","abc","bhavani"]
if(attendees.count ("saibhavani")> 0):
    print(attendees.index("saibhavani"))

#update operation
attendees =["bhavani","chinni","sravya"]
attendees[2] = ("saibhavani")
print(attendees)

attendees =["bhavani","chinni","sravya"]
attendees1 =["saibhavani","laxmi"]
attendees.extend(attendees)
print(attendees)

#delete operation
lst=["bhavani","chinni","sravya"]
lst.remove("chinni")
print(lst)

lst=["bhavani","chinni","sravya"]
lst.remove("bhavani")
print(lst)

lst=["bhavani","chinni","sravya"]
lst.pop(2)
print(lst)

lst=["bhavani","chinni","sravya"]
lst.pop()
lst.pop()
print(lst)
