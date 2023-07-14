import datetime
import openpyxl

def check_valid_date(y, m, d):
    correctDate = None
    try:
        newDate = datetime.datetime(y, m, d)
        correctDate = "Valid Date"
        myfile = openpyxl.load_workbook("event.xlsx")
        sheet = myfile.get_sheet_by_name("Sheet1")
        sheet['A2'] = "My BirthDay"
        event_date = str(y) + '-' +str(m) + '-' + str(d)
        print(event_date)
        sheet['B2'] = event_date
        myfile.save('event.xlsx')
    except ValueError:
        correctDate = "Invalid Date"
    return correctDate

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
print(check_valid_date(year, month, day))
