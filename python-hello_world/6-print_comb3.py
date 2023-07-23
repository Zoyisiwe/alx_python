
for digit2 in range(10):
    for digit3 in range(digit2 + 1, 10):
        print(f"{digit2}{digit3:01d}" .format(digit2,digit3), end=" ")
