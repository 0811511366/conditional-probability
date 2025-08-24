def a_and_b(a,b):
    if a==1:
        prob_student=0.3
        if b==1:
            prob_dining=0.75
        else:
            prob_dining=0.25
        print(f"probability of a given b: {prob_dining}")
    if a==2:
        prob_student=0.7
        if b==1:
            prob_dining=0.6
        else:
            prob_dining=0.4
        print(f"probability of a given b: {prob_dining}")
    prob_a_and_b=prob_student*prob_dining     
    return round(prob_a_and_b,3) 


print("check the prob of anyevent occuring\nenter your choices:")
print("is the student  a freshman?\n1.yes\n2.no")
a=int(input("enter your choice: "))

print("is  the student eating in dinning hall?\n1.Yes\n2.No")
b=int(input("enter your choice:"))        

print(f"the prob of both events happening us: {a_and_b(a,b)}")