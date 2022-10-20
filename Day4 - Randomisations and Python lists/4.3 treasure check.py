import random

row1 = ["✅" , "✅" , "✅"]
row2 = ["✅" , "✅" , "✅"]
row3 = ["✅" , "✅" , "✅"]
map = [row1  , row2 , row3]
print(f"{row1}\n{row2}\n{row3}")

place = input(print("Where do you want to put Treasure ? "))
col = int(place[0])
row = int(place[1])
selected_row = map[row-1]
selected_row[col-1] = "❌"

print(f"{row1}\n{row2}\n{row3}")
