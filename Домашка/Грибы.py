num = int(input())
if num // 100:
    print("Грибов")
elif num // 10 % 10:
    print("Гриба")
elif num % 10:
    print("Грибов")

