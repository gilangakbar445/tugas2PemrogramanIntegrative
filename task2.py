total = 0.0
while True:
    x = float(input("Enter number : "))
    if x == float(-1):
        break
    number = float(x)
    total += number
print(total)