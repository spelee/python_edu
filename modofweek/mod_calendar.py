import calendar

# The calendar module defines the Calendar class

# https://pymotw.com/3/calendar/index.html

# --------------------------------------------------

# prmonth() produces formatted text output for a month
# configures TextCalendar to start weeks on Sunday.  Default is Monday.
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2017, 3)


# --------------------------------------------------

# Similar HTML table with HTMLCalendar and formatmonth()
# Each table cell has a class attribute corresponding to the day of the week, so the HTML can be styled through CSS

print("\n", "="*80, "\n")
chtml = calendar.HTMLCalendar(calendar.MONDAY)
print(chtml.formatmonth(2017, 7))

# --------------------------------------------------

# yeardatescalendar returns a list of month rows.
# Each month row contains up to 'width' months (defaulting to 3)
# Each month contains between 4 and 6 weeks
# each week contains 1-7 days.

print("\n", "="*80, "\n")

month_width = 3
c2 = calendar.HTMLCalendar(calendar.SUNDAY)
mrs2 = c2.yeardatescalendar(2018, width=month_width)

# mrs2 is a list of month rows, each of which is
# a lists 'width' number of months, each of which is
# a list of weeks...
for mr in mrs2:
    print("next {} month(s)...".format(month_width))
    for m in mr:
        print("new month...")
        for w in m:
            None
            # print("new week of {} days...".format(len(w)))
            for d in w:
                None
               # print(d)


# --------------------------------------------------

# Calculate the dates and organize the values into week and month ranges, then iterate over the result.
# Ultimate element is a tuple.  Days that

print("\n", "="*80, "\n")

cal = calendar.Calendar(calendar.SUNDAY)

m_w = 4
cal_data = cal.yeardays2calendar(2017, m_w)
print('len(cal_data)    :', len(cal_data))


print("{} groups of {} months.".format(len(cal_data), m_w))
for months_row in cal_data:
    print("next {} month(s)".format(m_w))
    for m in months_row:
        print("new month...")
        for w in m:
            print(" new week...")
            for d in w:
                print("  d type:{} value:{}".format(type(d), d))
                #print("    elem 1 type: {}".format(type(d[0])))
                #print("    elem 2 type: {}".format(type(d[1])))

# --------------------------------------------------

#
#

print("\n", "="*80, "\n")

print("calendar.day_name: {}".format(type(calendar.day_name)))
print("looped and printed...")
for dn in calendar.day_name:
    print("type: {}\tvalue: {}".format(type(dn), dn))
