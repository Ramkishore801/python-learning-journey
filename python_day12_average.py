numbers = []

n = int(input("How many numbers: "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

average = sum(numbers) / n

print("Average:", average)
