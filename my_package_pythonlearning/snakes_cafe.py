from textwrap import dedent

menu = {
    'Appetizers' : {
      'wings':0,
        'cookies':0,
        'spring rolls':0
    },
    'Entrees': {
        'salmon':0,
        'steak':0,
        'meat tornado':0,
        'a literal garden':0,

    },
    'Desserts': {
        'ice cream':0,
        'cake':0,
        'pie':0,
    },
    'Drinks': {
        'coffee':0,
        'tea':0,
        'blood of the innocent':0,
    }

}

def namaste():
    line_1 = '**************************************'
    line_2 = 'Welcome to the Snakes Cafe'
    line_3 = ' Here is our Menu '
    line_4 = 'To quit at any time, Please type "quit"'

    print(dedent(f'''
        {line_1}
        {'**' + line_2 + '**'}
        {'**' + line_3 + '**'}
        {'**                                   **'}
        {'**' + line_4 + '**'}
        {line_1}
    '''))

def place_order():
    print(dedent(f'''
    {'****************************************'}
    {'* What would you like to place order   *'}
    {'****************************************'}
    '''))

def our_menu():
    for cuisine_course in menu:
        print(menu[cuisine_course])
        print(cuisine_course)
        print('-' * len(cuisine_course))
        for item in menu[cuisine_course]:
            print(item.title())
        print('\n')

def process_order(order):
    
    menu_found = False

    for cuisine_course in menu:

        if order in menu[cuisine_course]:
            menu[cuisine_course][order] += 1
            print(f' You have {menu[cuisine_course][order]} {order} added to your list')
            menu_found = True
            break

    if not menu_found:
        print('Sorry, We are out of this Menu Item')
      
if __name__ == '__main__':
    namaste()
    our_menu()
    place_order()
    order = None
    while order != 'quit':
        order = input()
        if order.lower() == 'cheque' or order.lower() == 'quit':
         print('Thanks for Visiting us')
         break
        process_order(order.lower())