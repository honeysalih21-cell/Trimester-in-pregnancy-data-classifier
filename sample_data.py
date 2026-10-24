weeks = int(input("Enter gestational age in weeks: "))
if weeks >= 1 and weeks < 13:
    print("First trimester")
elif weeks >= 13 and weeks < 26:
    print("Second trimester")
elif weeks >= 26 and weeks <= 43:
    print("Third trimester")
else:
    print("Invalid weeks")
