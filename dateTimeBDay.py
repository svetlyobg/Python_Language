userInput = input("Please enter your birthday (mm/dd/yyyy)")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y").date()
print(birthday)
days = birthday - currentDate
print(days.days)
