def line():
    print('-'*50)


def header(msg):
    line()
    print(msg.center(50))
    line()


def readint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print('\033[1;31mInvalid format, try Again...\033[m')
        except KeyboardInterrupt:
            print('The User preferred to not continue')


def menu(lst):
    header('CSV CLIENTS MANAGEMENT')
    for i, o in enumerate(lst):
        print(f'{i+1} - {o}')
    line()
    opt = readint('Your Option: ')
    line()
    return opt