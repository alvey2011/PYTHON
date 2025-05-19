w = float(input("enter ur weight in kg :"))
h = float(input("enter ir hight in metere :"))

bmi = w / h **2

print("your BMI is ", round (bmi,2))

if bmi < 18.5:
    print("You are undewight. Please gain some weight.")

elif 18.5 <= bmi <= 24.9 :
    print("You are normal wight ,keppt it up")

elif 25 <= bmi <= 29.9 :
    print("You are overweight . Please loose some weight to become fit.")

elif 30 <= bmi <= 34.9 :
    print("You are obese . Lossing wight is emargancy !")
    
else:
    print ("You are extremly obease . You are is health rish . VISIT the doctor   ")
