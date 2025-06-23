w =float(int(input("enter ur weight in kg :")))
h = float(int(input("enter ur height in cm :")))
h = h / 100 # convert height from cm to meters
bmi = w / h  **2

print("ur bmi is",round(bmi,2))

if bmi < 18.5:
    print("ur underweight.pls eat more ")
elif 18.5 <=bmi  <= 24.9:
    print("ur normal weight .keep it up. ")
elif 25 <=bmi <=29.9 :
    print("ur overwight.pls i request u to exercise more.")
elif 30 <=bmi <=34.9:
    print("ur obese. pls i request u to lose weight. ur so unhealthy.")
else:
    print ("ur extremely obese . pls pls pls i request u to lose weight. ur so unhealthy."
          "u can die any moment. pls dont take care of urself.")