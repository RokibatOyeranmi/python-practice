while True:
    print('====EXPENSE TRACKER=====')
    print('1.Add expense')
    print('2.view expense')
    print('3.calculate total')
    print('4. Exit')
    choice = input('Choose an option')

    if choice == '1':
        print('you selected Add expenses')
    elif choice == '2':
        print('you selected view expenses')
    elif choice == '3':
        print('you selected Calculate total')
    elif choice == '4':
        print('Goodbye')
        break
    else:
        print('Invalid option, try again')
