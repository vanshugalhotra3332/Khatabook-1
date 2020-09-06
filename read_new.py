
#  https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/

from datetime import date
import datetime
import pandas as pd
import re
df = pd.read_csv("csv/csv_file_name") # paste your csv in folder named csv


#print(df.head())        # TO PRINT FIRST 5 ROWS OF THE DATAFRAME
#print(df.shape)          #TO KNOW ROWS,COLUMNS (ORDER)
df.fillna(0, inplace=True)
#checking
#print(df.head(74))

#rows
#row1 = df.iloc[0]
#date =  ""         #in dd/mm/yyyy order

def search_by_name(name):
    lst=[]
    for i in range(len(df)):
        narration = df.iloc[i][-1]
        if re.search(name, str(narration)):
            lst.append(df.iloc[i])
        else:
            continue
    return lst

def credit_and_debit(lst):
    total_debited=0
    total_credited=0
    for i in lst:
        total_credited += i[3]
        total_debited +=  i[2]
    return "deposit =",total_credited, "Withdrawal =",total_debited

def search_by_date(date):
    lst=[]
    for i in range(len(df)):
        narration = df.iloc[i][0]         # searching date from each row
        if str(date) == str(narration):
            lst.append(df.iloc[i])
        else:
            continue
    return lst

def search_between_dates(date1,date2):
    lst_dates=[]
    lst_details=[]
    a= datetime.datetime.strptime(date1, '%d/%m/%Y')
    b =datetime.datetime.strptime(date2, '%d/%m/%Y')
    d1 = date(a.year,a.month,a.day)          # strip date fromat
    d2 = date(b.year,b.month,b.day)
    total_days =  abs((d2-d1).days)           #  no. of days between two dates 
    if total_days<=1000:                                         
        for i in range(total_days+1):
            if (d1>d2):                                    
                all_dates = d2 + datetime.timedelta(days=i)    # timedelta used for finding difference bewtween two dates.
                all_date = datetime.datetime.strptime(str(all_dates), "%Y-%m-%d").strftime("%d/%m/%Y")     # changing date format
                lst_dates.append(all_date)
                
            else:
                all_dates = d1 + datetime.timedelta(days=i)
                all_date = datetime.datetime.strptime(str(all_dates), "%Y-%m-%d").strftime("%d/%m/%Y")
                lst_dates.append(all_date)

    for j in range(len(df)):
       if df.iloc[j][0] in lst_dates:
           lst_details.append(df.iloc[j])
    return lst_details


while True:
    print("--------------------  Passboook Details  -------------------------")
    print(" 1. Search details by name")
    print(" 2. Search details on a particualr date")
    print(" 3. Search between two dates")
    print("4. Exit")
    n = int(input("Enter the No.:" ))
    if n ==1:
        name =input("Enter Name: ").upper()
        lst1=search_by_name(name)
        print(lst1,"\n")

        print("------------------------------------------------------------")
        print("Total Credit and Debited cash: \n",credit_and_debit(lst1))

    if n == 2:
        dat = input("Enter the date:")     #"26/05/2020"
        lst2 = search_by_date(dat)
        print(lst2 ,"\n")

        print("-----------------------------------------------------------")
        print("Total Credit and Debited cash: \n",credit_and_debit(lst2))
    if n==3:
        date1 = input("Enter the date1: (in format: dd/mm/yyyy)  = ")
        date2 = input("Enter the date2:")
        lst3 = search_between_dates(date1,date2)
        print(lst3,"\n")
        print("------------------------------------------------------------")
        print("Total Credit and Debited cash: \n",credit_and_debit(lst3))
    if n==4:
        break
    else:
        print("Selct correct Options")
