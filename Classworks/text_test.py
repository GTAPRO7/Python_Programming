print("Hello World")

##Lists

ListOne = [0,1,2,3,4,5,6,7,8,9]
ListTwo = ["apple", "mango", "orange", "jackfruit", "watermelon"]
print(ListOne)
print(ListTwo)
ListThree = ListOne + ListTwo
print(ListThree)
print("\nExecuting Slicing............")
slc1 = ListOne[0:3]
print(slc1)
##DemoPop = ListOne.pop()
##print(ListOne)

ListCopy = ListOne.copy()
print("\n")
print(ListCopy)

print("\n")
FirstTuple = (0,1,2,3,4,5,6,7,8,9)
SecondTuple = ("apple", "mango", "orange", "jackfruit", "watermelon")
print(FirstTuple)
print(SecondTuple)
ConvList = list(FirstTuple)
print(ConvList)

CombList = (ListOne + ListTwo + ConvList)
print(CombList)

##Write a python program to check the string recieved from the user is palindrom or not

##print("\n")
##print("Palindrom Checker..........")
##str1 = input("Please enter the string you want to check :")

##str2 = str1[::-1]

##if(str1 == str2):
##	print("Its a palindrom")
##else:
##	print("Not a palindrom")

print("\n")
ClgList = ["Christ", "Jain"]
TailList = ["College", "University"]
print("Through Indexing..........")
ClgTailList = [ClgList[0] + TailList[0], ClgList[1] + TailList[1], ClgList[0] + TailList[1], ClgList[1] + TailList[0]]
print(ClgTailList)
print("Through List Comprehension...........")
ClgTailList2 = [x + y for x in ClgList for y in TailList]
print(ClgTailList2)

