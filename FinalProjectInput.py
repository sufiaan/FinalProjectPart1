"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

Final Project Part 1
"""

import csv  # importing csv to read and write csv files
import operator # operator module for sorting items
import datetime

# Make the empty lists to append the contents of csv files

manufacturer_list = []
with open("ManufacturerList.csv") as file1:
    ml_reader = csv.reader(file1)
    for line in ml_reader:
        manufacturer_list.append(line)

price_list = []
with open("PriceList.csv") as file2:
    pl_reader = csv.reader(file2)
    for line in pl_reader:
        price_list.append(line)

service_dates_list = []
with open("ServiceDatesList.csv") as file3:
    sdl_reader = csv.reader(file3)
    for line in sdl_reader:
        service_dates_list.append(line)

# use operator module's itemgetter to sort the list by order id which is at index 0
sorted_manufacturerList = (sorted(manufacturer_list, key=operator.itemgetter(0)))

sorted_priceList = (sorted(price_list, key=operator.itemgetter(0)))

sorted_ServiceDatesList = (sorted(service_dates_list, key=operator.itemgetter(0)))

for x in range(len(sorted_manufacturerList)):
    sorted_manufacturerList[x].append(price_list[x][1])

for x in range(len(sorted_manufacturerList)):
    sorted_manufacturerList[x].append(service_dates_list[x][1])

final_list = sorted_manufacturerList

full_inventory = (sorted(final_list, key=operator.itemgetter(1)))

with open('FullInventory.csv', 'w') as output1:
    fi_write = csv.writer(output1)

    for x in range(len(full_inventory)):
        fi_write.writerow(full_inventory[x])

item_type = final_list

tower_list = []

laptop_list = []

phone_list = []

for i in range(len(item_type)):
    if item_type[i][2] == "tower":
        tower_list.append(item_type[i])

    elif item_type[i][2] == "phone":
        phone_list.append(item_type[i])

    elif item_type[i][2] == "laptop":
        laptop_list.append(item_type[i])

# Writing a file for each item type
with open('LaptopInventory.csv', 'w') as laptop:
    laptop_write = csv.writer(laptop)

    for x in range(len(laptop_list)):
        laptop_write.writerow(laptop_list[x])

with open('PhoneInventory.csv', 'w') as phone:
    phone_write = csv.writer(phone)

    for x in range(len(phone_list)):
        phone_write.writerow(phone_list[x])

with open('TowerInventory.csv', 'w') as tower:
    tower_write = csv.writer(tower)

    for x in range(len(tower_list)):
        tower_write.writerow(tower_list[x])

psd_list = []

for x in range(len(item_type)):
    if datetime.datetime.strptime(item_type[x][5], '%m/%d/%Y') < datetime.datetime.now(): # compare the service past service dates with today
        psd_list.append(item_type[x])
with open('PastServiceDateInventory.csv', 'w') as psd:
    psd_inventory_write = csv.writer(psd)
    psd_list = (sorted(psd_list, key=operator.itemgetter(5)))
    for x in range(len(psd_list)):
        psd_inventory_write.writerow(psd_list)

damaged_list = []

for x in range(len(item_type)):
    if item_type[x][3] == "damaged":
        damaged_list.append(item_type[x])

with open('DamagedInventory.csv', 'w') as damage:
    damage_write = csv.writer(damage)
    damaged_list = (sorted(damaged_list, key=operator.itemgetter(4), reverse=True))
    for x in range(len(damaged_list)):
        damage_write.writerow(damaged_list[x])
