#Que. Given the lengths of sides AB and BC of a right triangle, calculate the angle MBC in degrees. Print the angle rounded to the nearest integer followed by the degree symbol (°).

import math

ab = int(input())
bc = int(input())

print(f"{round(math.degrees(math.atan(ab / bc)))}\u00B0")