print("When are you leaving?")
starting_day_string = input()
starting_day_int = int(starting_day_string)
print(starting_day_int)
returning_day_int = int(raw_input("how many days are you leaving for:")) 
print(returning_day_int)

returning_day = starting_day_int + returning_day_int

print("You will come back on day: ", returning_day % 7)

def day_num_to_name(num):

    if num == 0:

        return "Sunday"

    if num == 1:
leave_day = int(input("What day are you leaving? (0-6)"))

away_days = int(input("How many nights are you gone?"))
day_back = (leave_day + away_days)

print("You will return on a",day_num_to_name(day_back))