run = True
while run:
    user_input = int(input('Pick A Number from 1-100: '))
    if user_input == 7:
        print('Thats Right, You won!')
    if user_input < 7:
        print('too low!')
    if user_input > 7:
        print("Too High!")
    else:
        print('{attempt} left.')
        attempt -= 1
        continue
    