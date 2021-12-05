#Tax Calculator

'''input data from user'''
print("****************Enter Shopping Cart Contents******************") 

'''input() function in python to take input from user'''
for i in range(2):
    input_data = input() 
    
    '''split() function in python to split the input contents'''
    split_data = input_data.split(' ')
    #print(split_data)
    length = len(split_data)
    '''print("**************data after split in quantity, name of item and price**************")'''
    Quantity = split_data[0]
    Item_desc = split_data[1:length-2] 
    Import_field = Item_desc[0]  
    #print(Import_field) 
    Item_field = Item_desc[0] 
    #print(Item_field) 
    Price = float(split_data[length-1])
    
    # Name_of_Item is not Food or Medicines or book
    if  Import_field in ['imported'] and Item_field not in ['book','food','medicine','chocolate']:
        #15%
        tax = ((Price * 15.0)/100)
        Price_upd = Price + tax
        print("price with including tax 15%")
        print(round(Price_upd,2))
    elif Import_field in ['imported']:
        #5%
        tax = ((Price * 5.0)/100)
        Price_upd = Price + tax
        print("price including tax 5%")
        print(round(Price_upd,2))
    elif Item_field not in ['book','food','medicine','chocolate','headache']:
        #10%
        tax = ((Price * 10.0)/100)
        Price_upd = Price + tax
        print("price including tax 10%")
        print(round(Price_upd,2))
    else:
        #0%
        print("price without tax 0%")
        print(round(Price,2))