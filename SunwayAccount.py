def initial_display():
    print('''
                   Sunway College Account Department
                          Maitidevi,Kathmandu
                              Welcome to
                  Salary Tax Calculation System (STCS) 
-----------------------------------------------------------------------------------                                  
    ''')


def calculate_tax_of_unmarried(salary):
    income=salary*12
    if(income<=400000):
        tax_amount=income * 0.01
    elif(income>400000 and income<=500000):
        tax_amount=(400000*0.01)+ ((income-400000)*0.10)
    elif(income>400000 and income<=700000):
        tax_amount=(400000*0.01)+ ((100000)*0.10)+(income-500000)*0.20
    elif(income>400000 and income<=1300000):
        tax_amount=(400000*0.01)+ ((100000)*0.10)+((200000)*0.20) + (income-700000)*0.30
    elif(income>=2000000):
        tax_amount=(400000*0.01)+ (income-400000*0.36)
    return tax_amount  

def calculate_tax_of_married(salary):
    income=salary*12
    if(income<=450000):
        tax_amount=income * 0.01
    elif(income>450000 and income<=550000):
        tax_amount=(450000*0.01)+ ((income-450000)*0.10)
    elif(income>450000 and income<750000):
        tax_amount=(450000*0.01)+ (100000*0.10)+(income-550000)*0.20
    elif(income>450000 and income<1300000):
        tax_amount=(450000*0.01)+ (100000*0.10)+(200000*0.20)+(income-7500000)*0.30
    elif( income>2000000):
        tax_amount=(400000*0.01)+ (income-400000*0.36)
    return tax_amount       


def display(name,address,pan,salary,taxamount,foryear):
    initial_display()
    print(f'''
     Name of the staff: {name}                                      Address: {address}
     PAN no: {pan}                                                  For Year:{foryear}
     Monthly salary: {salary}
    ''')   
    if(salary*12<=400000):
        slab="1%"
    elif(salary*12<=500000):
        slab="10%"
    elif(salary*12<=600000):
        slab="20%" 
    elif(salary*12<=1000000):
        slab="30%"
    elif(salary*12>2000000):
        slab="36%"               
    
        print(f'''
        Staff {name} with PAN {pan} fall under {slab} Tax salb.
        {name} with (PAN {pan}) has+ to pay tax to government is [Rs.]= {taxamount}
    ''') 


def staff_info():
    staffname=[]
    staffaddress=[]
    staffpan=[]
    StaffYear=[]
    staffincome=[]
    taxamount=[]
    staffno=int(input("Enter the number of staff you want to provide data: "))
    for i in range(staffno):
        staffname.append(input(f"Enter the name of the staff [{i+1}]:"))
        staffaddress.append(input(f"Enter the address of the staff [{i+1}]: "))
        staffpan.append(input(f"Enter the PAN.no of the staff [{i+1}]: "))
        StaffYear.append(input(f"Enter the year for which you want to calculate the tax[{i+1}]: "))
        staffincome.append(int(input(f"Enter the income of the staff in one month[{i+1}]: ")))
        married=input("Enter 'Y' for Married and 'N' for Unmarried Status: ")
        if(married=="Y"):
            taxamount.append( calculate_tax_of_married(staffincome[i]))
        else:
            taxamount.append( calculate_tax_of_unmarried(staffincome[i]))
    for i in range(staffno):
            display(staffname[i],staffaddress[i],staffpan[i],staffincome[i],taxamount[i],StaffYear[i])
            f=open("Puja.txt","a")
            f.write("Staff name: "+staffname[i]+", ")
            f.write("Staff address: "+staffaddress[i]+", ")
            f.write("Staff PAN: "+staffpan[i]+", ")
            f.write("For Year: "+StaffYear[i]+", ")
            f.write("Staff income: "+str(staffincome[i])+", ")
            f.write("Tax amount: "+str(taxamount[i])+"\n")
            f.close()
staff_info()