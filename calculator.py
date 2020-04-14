import re

print('Calculator')
print("Enter 'quit' to exit.")

run = True


def perform_maths():
    global run
    previous = 0
    equation = ""
    if previous == 0:
        equation = input('Enter equation: ')
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print('Goodbye!')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.!?:]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print('The answer is: ', previous)


while run:
    perform_maths()

