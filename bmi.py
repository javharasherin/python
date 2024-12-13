h=float(input("enter hieght"))
w=float(input("enter the weight"))
def bmi(w,h):
    bmi=(w)/(h/100)**2
    return bmi
data=(bmi(w,h))
print(data)