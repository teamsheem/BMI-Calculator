print ("Welcome to Our BMI and BFP calculator! Please enter details below and use lower case for gender")
weight= float(input("enter weight in pounds"))
height= float(input("enter height in feet"))
height = height*12
age= int(input("enter age"))
gender= str(input("enter gender (m for male, f for female, b for boy, and g for girl)"))
bmi= weight/(height*height)*703
print("this is your BMI  "+ str(bmi))
bfp = 0
if gender == ("m"):
  bfp= (1.2*bmi)+(.23*age)-16.2
  print( "this is your BFP  "+ str(bfp))
elif gender == ("f"):
  bfp= (1.2*bmi)+(.23*age)-5.4
  print("this is your BFP  "+ str(bfp))
elif gender == ("b"):
  bfp= (1.51*bmi)+(.7*age)-2.2
  print ("this is your BFP  "+ str(bfp))
elif gender == ("g"):
  bfp= (1.51*bmi)+(.70*age)-1.4
  print ("this is your BFP  "+ str(bfp))
  
