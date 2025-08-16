size = int(input("Input: "))
print("\nExpected Output:\n")
sizes = {
    29: "Small",
    30: "Medium",
    38: "Large",
    42: "XLarge"
}
print(sizes.get(size, "Invalid"))
