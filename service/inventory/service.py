def inventory_service():
    while True:
        inventory = [{potions: 0}, 
                     {heavyarmor: 0}, 
                     {lightarmor: 0}, 
                     {sword: 0},
                     {bow: 0},
                    {gold: 0}]
        print('welcome to the inventory ' \
        '\n -1- use item \n -2- equip item ' \
        '\n -3- exit')
        option = int(input())
        if option == 1:
            print('what item do you want to use?')
            print(inventory)

        