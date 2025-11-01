#import helper
from helper import validate_and_execute, user_input_message

import logging

logger = logging.getLogger("MAIN")
logger.error("error happened in the app")





'''
user_input = ""
while  user_input != "exit":
    user_input = input("Hey user, enter a number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)

'''










''' 
#print(20 * 24 * 60)
#print("20 days are " + str(50) + " minutes")
#print(f"20 days are {50} minutes")
#from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

my_list = ["20", "30", "100"]
print(my_list[2])
my_dictionary = {"days": 20, "unit": "hours"}
print(my_dictionary["days"])


print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"35 days are {35 * calculation_to_units} {name_of_unit}")
print(f"35 days are {50 * calculation_to_units} {name_of_unit}")
print(f"35 days are {110 * calculation_to_units} {name_of_unit}")


def scope_check(num_of_days):
    print(name_of_unit)
    print(num_of_days)

days_to_units(20, "awesome")
days_to_units(35, "looks good!")

'''
