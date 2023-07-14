import datetime
import openpyxl
def check_date(y, m, d):
    correctDate= None
    try:
        newDate= datetime.datetime(y,m,d)
        correctDate= "Valid Date"
        myfile= openpyxl.load_workbook('event.xlsx')
        sheet= myfile.get_sheet_by_name('Sheet1')
        sheet['A2']= 'My Birthday'
        event_date= str(y)+ '-'+str(m)+'-'+str(d)
        sheet['B2'] = event_date
        myfile.save('event.xlsx')
    except ValueError:
        correctDate = "Invalid Date"
    return correctDate
day= int(input("Enter Day: "))
mon= int(input("Enter Month: "))
yr= int(input("Enter Year: "))
res=check_date(yr,mon,day)
print(res)


