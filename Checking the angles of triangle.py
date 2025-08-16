angles = input("Input: ").split()
angle1 = int(angles[0])
angle2 = int(angles[1])
angle3 = int(angles[2])
total = angle1 + angle2 + angle3
print("\nExpected Output:\n")
if total == 180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
