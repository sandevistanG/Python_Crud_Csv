import interface
import management
from time import sleep


arqq = 'clients.csv'
management.verifycreate(arqq)


while True:
    opt = interface.menu(['Register Client', 'Show All Clients', 'Search Client By Id', 'Delete Client', 'EDIT CLIENT', 'Exit'])

    if opt == 1:
        interface.header('Register New Client')
        management.registercsv(arqq)
        sleep(1)

    elif opt == 2:
        interface.header('CLIENT LIST')
        management.showdata(arqq)
        sleep(2)

    elif opt == 3:
        interface.header('Search Client ID')
        management.searchcsv(arqq)
        sleep(2)


    elif opt == 4:
        interface.header('DELETE CLIENT')
        management.deleteupdate(arqq, True)
        sleep(2)


    elif opt == 5:
        interface.header('EDIT CLIENT')
        management.deleteupdate(arqq, False)
        sleep(2)

    elif opt == 6:
        interface.header('FINISHING PROGRAM...')
        sleep(1)
        break


    else:
        print('\033[1;31mINVALID OPTION\033[m')