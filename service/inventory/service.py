def inventory_service():
    
    inventory = {'potion': 0, 'sword': 0, 'shield': 0, 'heavyarmor': 0, 'lightarmor': 0, 'bow':0, 'gold': 0}
    print(f'welcome to the inventory  {inventory}' 
        '\n -1- use item \n -2- equip item ' \
        '\n -3- exit')
    while True:
        option = int(input())
        if option == 1:
            print('what item do you want to use?')
            print(inventory)


        