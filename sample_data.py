import csv
data = [
    ["Patient_ID", "Weeks", "Trimester"],
    ["P001", 8, ""],
    ["P002", 20, ""],
    ["P003", 32, ""],
    ["P004", 12, ""],
    ["P005", 26, ""]
]
for patient in data[1:]:
    weeks = patient[1]
    
    if weeks <= 13:
        patient[2] = "First"
    elif weeks <= 27:
        patient[2] = "Second"
    else:
        patient[2] = "Third"
with open("pregnancy_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Done, file saved successfully!")
 
