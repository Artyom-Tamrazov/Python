num = int(input())
if num % 100 >= 11 and num % 100 <= 14:
    print("Грибов")
elif num % 10 == 1:
    print("Гриб")
elif num % 10 >= 2 and num % 10 <= 4:
    print("Гриба")
else:
    print("Грибов")



