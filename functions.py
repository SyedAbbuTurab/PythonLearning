def hello_func():
    print("Hello Function!")
hello_func()

def greeting_func(greetings):
    return '{} Function'.format(greetings)
print(greeting_func('Hello'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'CompSci', name='Hena', age=25)
