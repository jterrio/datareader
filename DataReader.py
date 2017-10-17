import xlrd
import json
from pprint import pprint

class item(): #Our objects of items with their features

    def __init__(self, name, price_history, weapon_type, rarity):

        self.name = name
        self.price_history = price_history
        self.weapon_type = weapon_type
        self.rarity = rarity


def makeItems():
    print("Making items...")
    checker = " " #checker will later be set to value in excel file
    item_array = [] #our array our objects
    y = 1
    while(checker != "NULL"):  #checks to see if we are at end of excel file
        if(str(sheet.cell_value(y, 0)) != "NULL"): 
            with open(str(sheet.cell_value(y, 0)) + ".json") as data_file: #opens a json file that has the same name as the name attribute
                data = json.load(data_file) #loads the content of file, which contains an array of its pricing history
            prices = data
            thing = item(sheet.cell_value(y, 0), prices, sheet.cell_value(y, 2), sheet.cell_value(y, 3)) #create an object with all of the dat from json and excel file
            item_array.append(thing) #append it to our object list
            
        y = y + 1 #increment and update our checker for the end of the file
        checker = sheet.cell_value(y, 0)
    print("Finished!")
    return item_array





file_location = "C:/Users/ForceM/AppData/Local/Programs/Python/Python35-32/item_prices/DataReader.xlsx" #opens a excel file with our data
print("Data Found!")
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
items = []
items = makeItems() 

    
