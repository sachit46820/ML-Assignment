import math
ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()  # the sort function is used here to sort the ages list
print("sorted list",ages)
print("The Min age is" , ages[0], "and The Max age is",ages[-1])
sum_of_min_age_max_age=ages[0]+(ages[-1]) # here we used the + operator for adding the min and max ages.
print("Sum of min age and max age ",sum_of_min_age_max_age)
ages.append(ages[0]+ages[-1]) # we again added the value to the given list using append method.
mid = len(ages) // 2
sum_age=0
if len(ages)%2==0:  # here we used the conditions to check the validation.
    median=(ages[mid]+ages[~mid])/2  
else:
    median=ages[mid]
for age in ages:
    sum_age=sum_age+age
average =round(sum_age/len(ages),2) # used the round function to round off the decimal places to a particular value.
print("Median",median)
print("Average",average)
print("range of ages list is",ages[-1]-ages[0])