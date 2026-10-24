data = [
    ["Patient_ID","Weeks","Trimister"],
    ["P001", 8, ""],
    ["P001", 20, ""],
    ["P001", 32, ""],
    ["P001", 12, ""],
    ["P001", 26, ""]
]    
for patient in data[1:]:
    weeks = patient[1]
    if weeks <= 13:
        patient[2] = "First"
    elif weeks <= 27:
        patient[2] = "Second"
    else:
        patient[2] = "Third" 
file = open("pregnancy_data.csv","w") 
file.write(str(data))
file.close()  
print("Done,file saved succesfully")
 
