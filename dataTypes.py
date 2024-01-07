x = "Hello World!"
y = 2
z = 2.2
a = 22j
b = b"Hello"
c = bytearray(5)

print(b)
print(c)

x = 1
y = 35656222554887711
y1 = 12E4
z = -32555225454545454

print(type(x))
print(type(y))
print((y1))
print(type(z))

# Lists
Courses = ['History', 'Math', 'Physics']
print(Courses[0])
print(Courses[-1])
print(Courses[0:2])
# Append adds the item to the end of the list
Courses.append('Art')
# Insert add the item at specific location of the choice
Courses.insert(0, 'CompSci')
print(Courses)

# Extend in Lists
Courses_2 = ['Hindi', 'Urdu']
Courses.extend(Courses_2)

# Remove method
Courses.remove('Math')
Courses.pop()
print(Courses.index('History'))  # Finding values

# Tuples -> Immutable object
tuple_1 = ('History', 'Math', 'Physics')
print(tuple_1[0])
print(tuple_1.index('History'))  # Finding values

# Sets
cs_courses = {'History', 'Math', 'Physics'}
art_courses = {'History', 'Math', 'Physics', 'Design'}
print(cs_courses.intersection(art_courses))
print(art_courses.difference(cs_courses))
print(cs_courses.union(art_courses))

# Dictionaries
student = { 'name': 'jhon', 'age': 25, 'courses' : ['History', 'Math', 'Physics']}
print(student['name'])
print(student.get('phone'))
student['phone'] = '555-555-5555'
print(student.get('phone'))
student['name'] = 'Jane'
print(student['name'])

