# This is a collatz sequence program


def collats(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    else:
        print (3 * number + 1)
        return 3 * number + 1


user_input = int(input("Enter an ineger:"))
while True:
    user_input = collats(user_input)
    if user_input == 1:
        break
    else:
        continue
