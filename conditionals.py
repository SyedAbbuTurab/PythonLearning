language = 'Java'

if language == 'Python':
    print('The language is Python')
elif language == 'Java':
    print('The language is Java')
else:
    print('No Match')


user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

a = [1, 2, 3]
b = [1, 2, 3]
c = [4,5,6]
d = c

# print(a == b)
# print(c == d)
# print(a is b)
# print(c is d)

# Loops and iterations
nums = [ 1, 2, 3, 4, 5]

for num in nums:
    print(num)


for i in range(1, 6):
    print(i)

