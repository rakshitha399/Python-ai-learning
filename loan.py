
age = 22
income = 21000 #32900
credit_score = 677

if age >=18:
    print("your eligible")
    if income >= 30000:
       
        if credit_score >=700:
            print("prime loan")
        elif credit_score>=600 and credit_score<700:
            print("Standard loan")
        else:
            print("High-risk loan")
        
    elif income >=20000 and income <=29000:
        if credit_score >=700:
            print("Standard loan")
        elif credit_score>=600 and credit_score<700:
            print("High-risk loan")
        else:
            print("not eligible")

    else:
        print("your nor eligible")
else:
    print("Not eligible")