#creating empty list to store values
namel=[]
addressl=[]
emaill=[]
itempricel=[]
itemqtyl=[]
totall=[]
netTotall=[]
discl=[]

def initialDisplay():
    print('''     SUNWAY BHATBHATINI STORE 
   \t KATHMANDU, NEPAL\n
   \t\t\t\t Date: 2022-12-22
    ''')
    
# #fuction for input and information
def initialInformation():
    n=int(input("Enter the number of customers: "))
    #first for loop for different customers
    for i in range(n):
        #input for details
        namel.append(input(f"Enter the name of customer [{i+1}]: "))
        addressl.append(input(f"Enter the address of customer [{i+1}]: "))
        emaill.append(input(f"Enter the email of customer [{i+1}]: "))
        itemno=int(input(f"Enter the number of items of customer : "))
        
        for j in range(itemno):
            totalPrice=0
            itempricel=int(input(f"Enter the price of item [{j+1}]: "))
            itemqtyl=int(input(f"Enter the quantity of item [{j+1}]: "))
            totalPrice=totalPrice+itempricel*itemqtyl
            totall.append(totalPrice)
            calculation(totall)  
                   
        initialDisplay()   
        displayInformation(namel,addressl,emaill,totall,discl,netTotall) 
        
    Action=int(input("Enter 1 to print the bill: \nEnter 2 to Create the bill in text file: \nEnter 3 to both print and create bill : "))
    if Action==1:
        displayInformation(namel,addressl,emaill,totall,discl,netTotall)
    elif Action==2:
        writeInformation(namel,addressl,emaill,totall,discl,netTotall)
    elif Action==3:
        displayInformation(namel,addressl,emaill,totall,discl,netTotall)
        writeInformation(namel,addressl,emaill,totall,discl,netTotall)
    else:
        print("Invalid Input")                                                                                                              
def calculation(totall):
    for i in range(len(totall)):
        totalPrice=totall[i]
    #discount calculation   
        discount=0
        if totalPrice<=5000:
            discount = totalPrice*0.05
        elif totalPrice<=7000:
            discount=(5000*0.05)+(totalPrice-5000)*0.08
        elif totalPrice<=10000:
            discount=(5000*0.05)+(2000*0.08)+(totalPrice-7000)*0.10
        else:
            discount=(5000*0.05)+(2000*0.08)+(3000*0.10)+(totalPrice-10000)*0.15
        # net amount after discount\ 
        
        netAmount=totalPrice-discount
        netTotall.append(netAmount)
        discl.append(discount)
        return netAmount,discount
    
#function for writing the information in text file
def writeInformation(namel,addressl,emaill,totall,discl,netTotall):
    for j in range(len(namel)):
        f= open("C:\data\puja.txt","w", encoding="utf-8")
        for i in range(1):
            f.write(f"Customer Name: {namel [j]}\n")
            f.write(f"Customer Address: {addressl[j]}\n")
            f.write(f"Customer Email: {emaill[j]}\n")
            f.write(f"Total Price: {totall[j]}\n")
            f.write(f"Discount: {discl[j]}\n")
            f.write(f"Net Amount: {netTotall[j]}\n")
        f.close()

# #function for displaying the information
def displayInformation(namel,addressl,emaill,totall,discl,netTotall):
 for i in range(len(namel)):
    print(f"Customer Name: {namel[i]}")
    print(f"Customer Address: {addressl[i]}")
    print(f"Customer Email: {emaill[i]}")
    print(f"Total Price            : {totall[i]}")
    print(f"Discount: {discl[i]}")
    print(f"Net Amount: {netTotall[i]}")
 
# #function call
initialDisplay()
initialInformation()
