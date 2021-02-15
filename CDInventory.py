#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KBrock, 2021-Feb-14, modified to replace inner data structure with dictionaries
#------------------------------------------#

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

print('\nThe Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()
    print()
    if strChoice == 'x':
        # (x) Exit the program if the user chooses so
        print("'CD' ya later! Bye!")
        break
    if strChoice == 'l':
        # (l) Load existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'id': lstRow[0], 'title': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('Your inventory has been loaded.  Choose option (i) to display')
    elif strChoice == 'a':
        # (a) Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': strID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
        print('\nTo save the entry, choose option (s).')
    elif strChoice == 'i':
        # (i) Display the current data to the user each time the user wants to display the data
        print('Here\'s what we currently have: \n')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep=', ')
    elif strChoice == 'd':
        # (d) Delete entry
        for row in lstTbl:
            print (*row.values(), sep = ', ')
        Remove = input('Which ID would you like to remove: ')
        rownum = -1
        for row in lstTbl:
            rownum += 1
            if row['id'] == Remove:
                print (*row.values(), sep = ', ')
                print ('^^^ Has Been Removed')
                del lstTbl[rownum]
    elif strChoice == 's':
        # (s) Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('\nYour entry has been saved to', strFileName)
    else:
        print('Please choose either l, a, i, d, s or x!')

