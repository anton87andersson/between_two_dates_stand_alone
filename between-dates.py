from dateutil.rrule import rrule, WEEKLY, MO, TU, WE , TH, FR, SA, SU
from datetime import date


'''
	####### Stand-alone version to get all dates for ex. every Monday between 2 dates ########


	Done by: Anton Andersson @ 2021-03-10
	Free to use by anyone.
	-----------------------
	
	How it works:


	Enter start-date in YYYY-MM-DD format: 2020-01-01
	Enter end-date in YYYY-MM-DD format: 2020-02-01

	Output:

	2020-01-01 
	2020-01-08 
	2020-01-15
	2020-01-22
	2020-01-29

	
'''

# The list where the dates will be stored
result_dates = []


week_days = {
	"Monday" : MO,
	"Tuesday" : TU,
	"Wednesday" : WE,
	"Thursday" : TH,
	"Friday" : FR,
	"Saturday" : SA,
	"Sunday" : SU
}


def get_dates(date_entry):
	year, month, day = map(int, date_entry.split('-'))
	return date(int(year), int(month), int(day))


def get_day(day_entry):
	return week_days[day_entry]


# Start date entry
while True:
	try:
		date_entry_start = input("Enter start-date in YYYY-MM-DD format: ")
	except ValueError:
		print("You need to enter valid date!")
		continue
	else:
		start_date = get_dates(date_entry_start)
		print("Added " + date_entry_start + " as starting date")
		break

 
# End date entry
while True:
	try:
		date_entry_end = input("Enter end-date in YYYY-MM-DD format: ")
	except ValueError:
		print("You need to enter valid date!")
		continue
	else:
		end_date = get_dates(date_entry_end)
		print("Added " + date_entry_end + " as end date")
		break

# Get the days name (ex. Monday)
dayOfWeek = get_day(start_date.strftime('%A'))


for date in rrule(WEEKLY, byweekday=dayOfWeek, dtstart=start_date, until=end_date):
	# Add the dates into the result_date list
	result_dates.append(date)

# Print the date to console or change it to do whatever you want to do with all the dates
for i in result_dates:
	print(i)

