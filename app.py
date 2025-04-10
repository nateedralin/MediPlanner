print("Calorie Deficit Calculator: ")
print("")
gender = (input("Gender (M/F): ")).upper()
age = int(input("Age: "))
feet = int(input("Feet: "))
inches = int(input("Inches: "))
weight = int(input("Weight (lbs): "))
print("")
print("")
print("1 IF youare sedentary (little or no exercise)")
print("2 IF you are lightly active (light exercise or sports 1-3 days/week)")
print("3 IF you are moderately active (moderate exercise 3-5 days/week)")
print("4 IF you are very active (hard exercise 6-7 days/week)")
print("5 IF you are super active (very hard exerise and/or a physical job)")
print("")
exerciseFreq = int(input("How much do you exercise per week? Enter a number 1-5 corresponding to the layout above: "))

totalInches = ((feet * 12) + inches)
bmi = ((weight * 703) / (totalInches**2))
bfp =  ((1.20 * bmi) + (0.23 * age) - 10.8 - 5.4) / 100






def mifflinStJeor(pWeight, pHeight, pAge, pGender):
        if pGender == 'M':
            bmr = 66 + (6.23 * pWeight) + (12.7 * pHeight) - (6.8 * pAge)
            return bmr
        elif pGender == 'F':
              bmr = (655) + (4.35 * pWeight) + (4.7 * pHeight) - (4.7 * pAge)
              return bmr

def harrisBennedict(pWeight, pHeight, pAge, pGender):
        if pGender == 'M':  
            bmr = (88.362 + (13.397 * pWeight) + (4.799 * pHeight) - (5.677 * pAge))
            return bmr
        elif pGender == 'F':
            bmr = (447.593) + (4.35 * pWeight) + (4.7 * pHeight) - (4.7 * pAge)
            return bmr
          
def katchMcArdle(pWeight, pBfp ):
    bmr = (370 + (4.536 * (1 - pBfp) * pWeight))
    return bmr

def averageBmr(pWeight, pHeight, pAge, pBfp, pGender, funcM, funcH, funcK):
    total = funcM(pWeight, pHeight, pAge, pGender) + funcH(pWeight, pHeight, pAge, pGender) + funcK(pWeight, pBfp)
    average = total / 3
    return average




#print(mifflinStJeor(weight, totalInches, age), "calories")
#print(harrisBennedict(weight, totalInches, age), "calories")
#print(katchMcArdle(weight, bfp), "calories")
print("")
print("")
print("Your resting BMR:", round(averageBmr(weight, totalInches, age, bfp, gender, mifflinStJeor, harrisBennedict, katchMcArdle)))
if exerciseFreq == 1:
     print("Your BMR based on your activity level:", round(averageBmr(weight, totalInches, age, bfp, gender, mifflinStJeor, harrisBennedict, katchMcArdle))*1.2)
elif exerciseFreq == 2:
     print("Your BMR based on your activity level:", round(averageBmr(weight, totalInches, age, bfp, gender, mifflinStJeor, harrisBennedict, katchMcArdle))*1.375)
elif exerciseFreq == 3:
     print("Your BMR based on your activity level:", round(averageBmr(weight, totalInches, age, bfp, gender, mifflinStJeor, harrisBennedict, katchMcArdle))*1.55)
elif exerciseFreq == 4:
     print("Your BMR based on your activity level:", round(averageBmr(weight, totalInches, age, bfp, gender, mifflinStJeor, harrisBennedict, katchMcArdle))*1.725)
elif exerciseFreq == 5:
     print("Your BMR based on your activity level:", round(averageBmr(weight, totalInches, age, bfp, gender, mifflinStJeor, harrisBennedict, katchMcArdle))*1.9)



     
