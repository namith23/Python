import math
def paint_calc(height, width, cover):
  no_of_cans = (height * width)/coverage
  round_up = math.ceil(no_of_cans)
  print(f"You'll need {round_up} cans of paint.")

test_h = int(input()) # Heigh t of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)