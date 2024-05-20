#Define the menu list
menu = {
    'Pizza':40,
    'Burger':50,
    'salad':100,
    'cheese-cake':160,
    'Chicken-Burger':257,
    'coffee':57,
}

#Greet
print("welcome to the Restraunt")
print("Pizza: Rs40\nBurger: Rs50\nsalad: Rs100\ncheese-cake: Rs160\nChicken-Burger: Rs257\ncoffee: Rs57\n ")

order_total = 0

#user enter order
while True:
 item_1 = input("Enter the name of the item you want to order = ")
 if item_1 in menu:
    order_total+= menu[item_1] #0+50
    print("Ordered item {item_1} has been added to your order")
 else:
    print(f"Ordered item {item_1} is not available yet!")

 another_Order = input("Do you want to add another item? (Yes/No)")
 if another_Order == "Yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available yet! ")
 print(f"The total amount of item is to pay {order_total}")
 
 

    
    

