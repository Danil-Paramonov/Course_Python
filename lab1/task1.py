numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


numbers[4] = 0
middle = sum(numbers) / len(numbers)
numbers[4] = middle

print("Измененный список: " + str(numbers))