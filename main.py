print("write the medical cause ('Y' for yes 'N' for no)")
medical_cause = input("Enter Yes or No")

if medical_cause == 'Y' :
    print("You are allowed to take the exam")
else :
    attendence = int(input("write your attendence in number"))
    if attendence > 75 :
        print("You are allowed to take the exam")
    else :
        print("You are not allowed to take the exam")