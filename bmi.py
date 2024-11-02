def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi=(weight/(height*height))
    print("bmi is "+str(bmi))
    if bmi<18.5:
        print("It is under weight")
        return -1
    elif 18.5<=bmi<=25.0:
<<<<<<< HEAD
        print("It is normal weight") 
=======
        print("It is normal weight")
>>>>>>> a8a41a267b50edd343d720f4bbeb132ad82e85aa
        return 0
    elif bmi>25.0:
        print("It is ove weight")
        return 1
<<<<<<< HEAD
#calculate_bmi(weight=57,height=1.73)
=======
#calculate_bmi(weight=57,height=1.73)
>>>>>>> a8a41a267b50edd343d720f4bbeb132ad82e85aa
