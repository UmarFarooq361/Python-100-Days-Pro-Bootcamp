import math

height_t = int(input("Enter wall height : "))
width_t = int(input("Enter wall width : "))
coverage = 5

def paint_area_calc(height , width , cover):
    area = height * width
    no_of_cans = math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paint")

paint_area_calc(height= height_t  , width=width_t , cover = coverage)