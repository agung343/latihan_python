import math
wall_height = int(input("Height of wall: "))
wall_width = int(input("Width of wall: "))

def paint_calculator(height, width, paint_per_square):
    calculate = height * width / paint_per_square
    paint_needed = math.ceil(calculate)
    print(f"You need {paint_needed} bin")

paint_calculator(height=wall_height, width=wall_width, paint_per_square=5)
