weeks = int(input("Enter gestational age in weeks: "))
if weeks >= 1 and weeks <= 13:
    print("First trimester")
elif weeks >= 14 and weeks <= 27:
    print("Second trimester")
elif weeks >= 28 and weeks <= 43:
    print("Third trimester")
elif weeks > 43:
    print("Post term")
else:
    print("Invalid weeks")
