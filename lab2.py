def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi=(weight/(height*height))
    return bmi
bmiOutput=calculate_bmi(weight=57,height=1.73)
print("bmiOutput "+str(bmiOutput))