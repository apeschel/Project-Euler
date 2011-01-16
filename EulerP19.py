def isLeapYear(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

if __name__ == '__main__':
  (SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY) = range(7)
  (JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, 
  OCTOBER, NOVEMBER, DECEMBER) = range(12)
  month_len =  {JANUARY:31, 
                FEBRUARY:28, 
                MARCH:31, 
                APRIL:30, 
                MAY:31,
                JUNE:30,
                JULY:31,
                AUGUST:31,
                SEPTEMBER:30,
                OCTOBER:31,
                NOVEMBER:30,
                DECEMBER:31}
  sunday_start = 0
  cur_day = TUESDAY 

  for year in range(1901, 2000 + 1):
    for month in range(12):
      if cur_day == SUNDAY:
        sunday_start += 1
      days = month_len[month]
      if month == FEBRUARY and isLeapYear(year):
        days += 1
      cur_day = (cur_day + days) % 7
  print(sunday_start)
