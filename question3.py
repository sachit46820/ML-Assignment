brothers=('s','a','c','h','i','t')
sisters=('k','u','m','a','r')
siblings = brothers + sisters  #adding two tuples into one and assigning it to siblings
print(siblings)
print("Number of siblings : " + str(len(siblings))) # I have got 11 siblings
modify_list=list(siblings)  #As tuples are immutable we cannot add other elements.so we need to modify into list.
modify_list.append("jag") #adding element to list
modify_list.append("pad") #adding element to list
family_members=tuple(modify_list) #Then we need to covert back into tuple.
print(family_members)