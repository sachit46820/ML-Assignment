weight=float(input("the given set of weight:")) # float method is used to return a floating point number from given string
unit=input("given unit of weight:")
print("given weight is",weight,unit)
if unit.upper()=="LB": # returns the upper case string from the given string. And validates the condition. 
    converted = weight*0.45355
    unit1 = "kg"
    print("new weight is:", converted, unit1,'.')
else:
    converted = weight/0.45377
    unit2 = "pounds"
    print("New weight is:")