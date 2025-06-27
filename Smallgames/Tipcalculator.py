print("Welcome to the tip calculator!")
TotalBill = (float(input("Enter the total amout of your bill:\n")))
TipPercentae = (float(input("Enter the percentage on total amount that you want to tip:\n")))
TipAmount = (TipPercentae/100)*TotalBill
NoOfPerons = (float(input("Enter the total numer of person you want to split the bill with:\n")))
Billforeach = TotalBill/NoOfPerons
TipForEach = TipAmount/NoOfPerons
Bill_WIth_Tip = Billforeach + TipForEach
Roundedvalue = round(Bill_WIth_Tip, 2)
print("Each person should pay: ",Roundedvalue)