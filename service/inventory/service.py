def inventory_service():
    while True:    
        health = 100
        defense = 0
        atk = 0
        inventory = {'potion': 0, 'gold': 0}
        armor = {'shield': 0, 'heavyarmor': 0, 'lightarmor': 0}
        weapons = {'sword': 0, 'bow':0}
        print(f'welcome to the inventory  {inventory}' 
            '\n -1- use a potion ' \
            '\n -2- equip item ' \
            '\n -3- exit')
        
        option = int(input())
        if option == 1:
            for i,j in inventory.items():
                if i == 'potion' and j > 0:
                    print('you used a potion')
                    health += 30
                    inventory['potion'] -= 1
                    break
        elif option == 2:       
            print('do you wanna equip a weapon or armor?')
            option2 = int(input('1- weapon \n 2- armor \n'))
            if option2 == 1:
                enumerate_weapons = list(enumerate(weapons.keys(), start=1))
                option3 = int(input('select the weapon you want to equip \n'))
                
            
        elif option == 3:
            break
        
        