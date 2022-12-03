#Create python product Store
print("Enter Customer Name")
customer=str(input())
product=["JavaScript","HTML5","CSS3","PHPMySQL","Python","C","C++","C#","Java","JQuery"]
print("Enter the name of the book you are looking for: ")
book=str(input())
if book ==(product[0]):
        info="This is JavaScript ES6 by Don Gosselin 2022 it has 709 Pages it cost of 300 pesos"
        price=300
        print(info)
        print("Do you want to buy it YES or NO?")
        answer=str(input())
        if answer=="YES" or answer=="yes":
           print("Enter quantity:")
           quantity=int(input())
           total=price*quantity
           print("the amount is ")
           print(total)
           print("Do you want to pay it? YES or NO")
           paid=str(input())
           if paid=="yes" or paid=="YES":
              print(customer+" Thank you for buying this "+quantity,book+" book")
elif book ==(product[1]):
        info="This is HTML5 by Don Gosselin 2022 it has 544 Pages it cost of 540 pesos"
        print(info)
        print("Do you want to buy it YES or NO?")
        answer=str(input())
        if answer=="YES" or answer=="yes":
           print("Enter quantity:")
           quantity=int(input())
           price=540
           total=price*quantity
           print("the amount is ")
           print(total)
           print("Do you want to pay it? YES or NO")
           paid=str(input())
           if paid=="yes" or paid=="YES":
              print(customer+" Thank you for buying this "+book+" book")
elif book ==(product[2]):
        info="This is CSS3 by Don Gosselin 2022 it has 674 Pages it cost of 780 pesos"
        print(info)
        print("Do you want to buy it YES or NO?")
        answer=str(input())
        if answer=="YES" or answer=="yes":
           print("Enter quantity:")
           quantity=int(input())
           price=780
           total=price*quantity
           print("the amount is ")
           print(total)
           print("Do you want to pay it? YES or NO")
           paid=str(input())
           if paid=="yes" or paid=="YES":
              print(customer+" Thank you for buying this "+book+" book")
elif book ==(product[3]):
        info="This is PHPMySQL by Don Gosselin 2022 it has 962 Pages it cost of 690 pesos"
        print(info)
        print("Do you want to buy it YES or NO?")
        answer=str(input())
        if answer=="YES" or answer=="yes":
           print("Enter quantity:")
           quantity=int(input())
           price=690
           total=price*quantity
           print("the amount is ")
           print(total)
           print("Do you want to pay it? YES or NO")
           paid=str(input())
           if paid=="yes" or paid=="YES":
              print(customer+" Thank you for buying this "+book+" book")
#elif book==(product[4] and product[5]):not working
elif book ==(product[4])or book==(product[5])or book==(product[6])or book==(product[7])or book==(product[8])or book==(product[9]):
     print("Sorry this book is not available to buy")
#elif book ==(product[5]):
#    print("Sorry this book is not available to buy")
#elif book ==(product[6]):
#     print("Sorry this book is not available to buy")
#elif book ==(product[7]):
#     print("Sorry this book is not available to buy")
#elif book ==(product[8]):
#     print("Sorry this book is not available to buy")
#elif book ==(product[9]):
#     print("Sorry this book is not available to buy")
else:
    print("sorry youre searching book is not on the list")
print("thank you for coming")