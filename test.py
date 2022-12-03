name="Joseph"
name1=str(input())
lastname="Morales"
lastname1=str(input())
number=int(input())
number2=float(input())
if (name1==name and lastname1 ==lastname) or (name1=="joseph" and lastname1=="morales"):
   print("Hi " +name1 +" "+ lastname1)
   if number> number2:
      print("the number is passed")
   elif number==number2:
      print("the number is draw")
   elif number< number2:
      print("the number is failed")
elif (name1!=name and lastname1!=lastname) or (name1==name and lastname1!=lastname) or (name1!=name and lastname1==lastname):
   print("Sorry we will not give you the result you type wrong name and last name ")
