##Sets

FirstSet = {0,1,2,3,4,5,6,7,8,9,9}
SecondSet = {"apple", "mango", "orange", "jackfruit", "watermelon"}
ThirdSet = {0,1,2,3,4,5,6,7,8,9,"apple", "mango", "orange", "jackfruit", "watermelon"}
print(FirstSet)
print(SecondSet)
print(ThirdSet)
FirstTuple = (0,1,2,3,4,5,6,7,8,9)
FirstList = [0,1,2,3,4,5,6,7,8,9]
print(type(FirstSet))
print(type(ThirdSet))
print(type(FirstTuple))
print(type(FirstList))
##FourthSet = {1,2,3,{4}} TypeError: unhashable type: 'set'
FifthSet = {(1,2),3,4,5}
##SixthSet = {1,2,3,[4,5]} TypeError: unhashable type: 'list'
##print(FourthSet)
print(FifthSet)
##print(SixthSet)

##Added Elements
print("\nDemostartion of Add..........")
FirstSet.add(10)
print("Added element 10 to First set", FirstSet)

##Update
print("\nDemostartion of Update..........")
FirstSet.update([11, 12])
print("Updated element 11, 12 to First set", FirstSet)

##remove
print("\nDemostartion of Remove..........")
FirstSet.remove(12)
print("Removed element 12 to First set", FirstSet)

##discard
print("\nDemostartion of Discard..........")
FirstSet.discard(11)
print("Discarded element 11 to First set", FirstSet)

##pop
print("\nDemostartion of Pop..........")
FirstSet.pop()
print("Poping element from First set", FirstSet)

##clear
print("\nDemostartion of Clear..........")
FirstSet.clear()
print("Clearing element from First set", FirstSet)

##Membership
print("\nDemostartion of Membership..........")
SeventhSet = {0,1,2,3,4,5}
EightSet = {5,6,7,8,9,10}
print(SeventhSet)
print(EightSet)
print("Set", SeventhSet)
print("Is 1 present :", 1 in SeventhSet)
print("Is 100 not in :", 100 not in EightSet)

##Set Operation
print("\nDemostartion of Set Operations..........")
print(SeventhSet)
print(EightSet)
Un = SeventhSet.union(EightSet)
Unp = SeventhSet | EightSet
Int = SeventhSet.intersection(EightSet)
IntA = SeventhSet & EightSet
Dif = SeventhSet.difference(EightSet)
print("Union of two sets :", Un)
print("Union of two sets using | :", Unp)
print("Intersection of two sets :", Int)
print("Intersection of two sets using & :", IntA)
print("Difference of two sets :", Dif)

##Supersets
print("Is SeventhSet superset of EightSet :", SeventhSet.issuperset(EightSet))
print("Is EightSet superset of  SeventhSet :", EightSet.issuperset(SeventhSet))

##DisjointSets
print("Are SeventhSet and EightSet disjoint? :", EightSet.isdisjoint(SeventhSet))

##FrozenSet

frz = frozenset([6,7,8,9,10])
print("Union with another set :", frz.union({11,12}))

##Create two sets of students, namely javastudents and pythonstudents. ##Write a command for the following
##Print students learning Python
##Print students learning Java
##Print students learning both Python and Java
##Print students learning either Python or Java
##Print students learning Python but not Java

javastd = {"Gokul", "Hari", "Donal", "Dixon", "Ashelle"}
pystd = {"Dhanashree", "Angel", "Lenny", "Ashelle", "Charles"}
print("Students learning Java are :", javastd)
print("Students learning Python are :", pystd)
print("Students learning both Python and Java :", javastd & pystd)
print("Students learning either Python or Java :", javastd.symmetric_difference(pystd))
print("Students learning Python but not Java :", pystd.difference(javastd))
print("Students learning Java but not Python :", javastd.difference(pystd))








