from datetime import datetime, timedelta
from icalendar import Calendar,Event

# open the text file containing the event details
f = open("data.txt","r")
f = f.read()
lines = f.split("\n")

# convert event details into a tuple -> (days_from_start, event_summary)
res = []
for i in range(len(lines)):
    cat = lines[i]
    if "â€“" in cat:
        res.append((i,cat.split("â€“")[1]))
    elif "â€”" in cat:
        res.append((i,cat.split("â€”")[1]))

# initialise start_date and define a day and an hour for creating times
start_date = datetime(2020, 12, 7,7,0,0)
day = timedelta(days = 1)
hour = timedelta(hours = 1)

# initialise a list called output, and keys for a dictionary
output = []
keys = ("start_time", "end_time","activity")
for i,j in res:
    # exclude rest days from calendar
    if 'Rest' in j:
        continue
    else:
        # create values for (start_time, end_time, activity)
        row_data = (start_date + i*day, start_date + i*day + hour,j)
        # zip the key and values together into a dictionary
        # insert each dictionary into a list
        output.append(dict(zip(keys,row_data)))

# use to test whether output is correct
# print(output)

# initialise a calendar object
cal = Calendar()
for row in output:
    # initialise an event for each date
    event = Event()

    # take values from the dictionary created above
    # give values to each attribute in the class called event
    event.add("summary",row["activity"])
    event.add("dtstart",row["start_time"])
    event.add("dtend", row["end_time"])
    event.add("description", row["activity"])
    #add the event into a calendar
    cal.add_component(event)

# create a new ics file
p = open('run_schedule.ics','wb')
# write the calendar into an ics file
p.write(cal.to_ical())
p.close()

    


