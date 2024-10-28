def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi=(weight/(height*height))
    print("bmi is "+str(bmi))
    if bmi<-1:
        print("It is under weight")
    elif bmi==0:
        print("It is normal weight") 
    elif bmi>1:
        print("It is ove weight")
calculate_bmi(weight=57,height=1.73)