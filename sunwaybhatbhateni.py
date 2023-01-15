def initialDisplay():
  first ="""SUNWAY BHATBHATENI STORE"""
  second ="""MAITIDEVI KATHMANDU"""
  third="""date: 2077/01/01"""
  print(first)
  print(second)
  print(third)
  print("---------------------------------------------------------")
# All the functions for input and other information

def inputinformation():
    n= int(input("Enter the number of customer"))
    for i in range (n):
        Name=input(f"Enter the name of customer [{i+1}]: ")
        Address=input(f"Enter the address of customer {i+1}: ")
        Email=input(f"Enter the email of customer {i+1}: ")
        item=int(input(f"Enter the number of items of customer : "))
    for j in range (item):
          totalPrice=0
          itemname=input(f"Enter the name of item {j+1}: ")
          itemprice=int(input(f"Enter the price of item {j+1}: "))
          itemqty=int(input(f"Enter the quantity of item {j+1}: "))
          totalPrice=totalPrice+itemprice*itemqty
      #callig functions
          netAmount,discount=calculation(totalPrice)
        #forbiling purpose 
          initialDisplay()
          displayInformation(Name,Address,Email,totalPrice,discount,netAmount)

#function for calculation of discount and Net amount
def calculation(totalPrice):
    discount=0
    if totalPrice<=5000:
        discount = totalPrice*0.05
    elif totalPrice<=7000:
        discount=(5000*0.05)+(totalPrice-5000)*0.08
    elif totalPrice<=10000:
        discount=(5000*0.05)+(2000*0.08)+(totalPrice-7000)*0.10
    else:
        discount=(5000*0.05)+(2000*0.08)+(3000*0.10)+(totalPrice-10000)*0.15
    # net amount after discount
    netAmount=totalPrice-discount
    return netAmount,discount

#function for displaying information by printing them
def displayInformation(name,address,email,totalPrice,discount,netAmount):

f=open("C:\data\practicepython.txt","w", encoding="utf-8")

# Write the output to the file
f.write(f"Customer Name: {name}\n")
f.write(f"Customer Address: {address}\n")
f.write(f"Customer Email: {email}\n")
f.write(f"Total Price: {totalPrice}\n")
f.write(f"Discount: {discount}\n")
f.write(f"Net Amount: {netAmount}\n")

# Close the file
f.close()
#function call
initialDisplay()
inputinformation()














































































































