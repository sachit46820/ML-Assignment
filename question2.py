dog={}
dog={'name':[],'color':[],'breed':[],'legs':[],'age':[]}
print(dog)
student={'first_name':[],'last_name':[],'gender':[],'age':[],'martial status':[],'skills':[],
'country':[],'city':[],'address':[]}
print(student)
print(len(student))     # gives the length of the student dictonary
print(student['skills'])
print(type(student['skills']))
student['skills']+=['singing','gaming'] # adding the values to the skills
print(student.keys())
print(student.values())