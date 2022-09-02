it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_it=len(it_companies)#length of it_companies
print(length_it)
it_companies.add("Twitter")     #Adding "Twitter" using add() method.
print(it_companies)
it_companies.update(["Wells Fargo","Dell" ,"Mahindra"])     #Adding multiple companies using update() method.
print(it_companies)
it_companies.remove("Apple")      #Deleting "Apple" using remove() method.
print(it_companies)
#it_companies.discard("Apple")#Deleting "Apple" using remove() method.
'''
The discard() method removes the specified item from the set.
This method varies from the remove() method, since the remove() method will show an error
if the specified item does not exist while the discard() method will not do as that.
'''
join_ab=A.union(B)
print(join_ab)
inter_ab=A.intersection(B)
print(inter_ab)
print(A.issubset(B))   # In order to test whether a is subset of b or not.
print(A.isdisjoint(B))  # In order to test whether A isdisjoint of B.
A,B=A.union(B),B.union(A)
print(A.symmetric_difference(B))#To find symmetric difference.
A.clear()    #To clear the whole set.
B.clear()    #To clear the whole set.
age_set=set(age)     #To convert it into set.
len_age_set,len_age=len(age_set),len(age)
print(len_age,len_age_set)  #lentgh of age is reduced by "3" after converting it into set as age has 3 duplicate elements.