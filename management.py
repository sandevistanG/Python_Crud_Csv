import csv
import interface


def verifycreate(arq):
    try:
        with open(arq, 'r', newline='', encoding='utf-8') as f:
            client_r = csv.reader(f)
            print('\033[1;32mFile Accessed\033[m')
    except FileNotFoundError:
        try:
            with open(arq, 'w', newline='', encoding='utf-8') as file:
                myheader = ['ID', 'NAME', 'AGE', 'CITY']

                c_write = csv.writer(file)
                c_write.writerow(myheader)
                print('\033[1;32mFile Created with header\033[m')
        except Exception as err:
            print(f'\033[1;31mSomething Went Wrong..., {err.__class__}\033[m')


def loaddata(arq):
    data = []
    with open(arq, 'r', newline='', encoding='utf-8') as filee:
        reader = csv.DictReader(filee)
        for line in reader:
            line['ID'] = int(line['ID'])
            line['AGE'] = int(line['AGE'])
            data.append(line)

    return data


def createig(arq):
    clients = loaddata(arq)
    if not clients:
        return 1
    else:
        lastId = clients[-1]['ID']
        return lastId + 1


def registercsv(arq):
    idd = createig(arq)
    name = str(input('Client Name: '))
    age = interface.readint('Age: ')
    city = str(input('City: '))

    row = [idd, name, age, city]

    with open(arq, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(row)
    print('\033[1;32mREGISTERED\033[m')


def showdata(arq):
    mydata = loaddata(arq)
    for c in mydata:
        print(f'ID: {c['ID']}  {c['NAME']:<18} {c['AGE']} YO {c['CITY']:>15}')


def searchcsv(arq, show=False):
    showdata(arq)
    interface.line()
    data = loaddata(arq)
    idd = interface.readint('ClIENT ID: ')
    interface.line()
    found = False

    for c in data:
        if idd == c['ID']:
            print('\033[1;32mCLIENT FOUND!\033[m')
            print(f'ID: {c['ID']}  {c['NAME']:<18} {c['AGE']} YO {c['CITY']:>15}')
            found = True
            return idd

    if not found:
        print('\033[1;31mCLIENT NOT FOUND\033[m')
        return False


def rewritecsv(arq, data):
    mydata = data
    myheader = ['ID', 'NAME', 'AGE', 'CITY',]

    with open(arq, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(myheader)
        for row in mydata:
            writer.writerow(row.values())


def deleteupdate(arq, dele=False):
    idd = searchcsv(arq)
    mydata = loaddata(arq)

    if idd:
        for c in mydata:
            if idd == c['ID']:

                if dele:
                    mydata.remove(c)
                    print('\033[1mCLIENT REMOVED!\033[m')
                    break
                else:
                    opt = interface.menu(['Change Name',
                          'Change Age',
                          'Change City'])
                    if opt == 1:
                        c['NAME'] = str(input('New Name: '))
                    if opt == 2:
                        c['AGE'] = interface.readint('New Age: ')
                    if opt == 3:
                        c['CITY'] = str(input('New City: '))
                    else:
                        print('INVALID OPTION')
                    print('\033[1mCLIENT UPDATED!\033[m')
                    break
        rewritecsv(arq, mydata)



