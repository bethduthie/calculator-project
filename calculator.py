import re

print('Calculator')
print("Enter 'quit' to exit.")

previous = 0
run = True


def perform_maths():
    global run
    global previous
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
    new = input('Do you want to start again? y/n')
    if new == 'y':
        previous == 0
    else:
        previous == eval(str(previous) + equation)


while run:
    perform_maths()

