# Given a person's first_name and last_name variables;

# Create the variables full_name and form the fullname by simply joining the first and last name together, separated by a space and first letters in capital
# Create the variables email and form the email by joining the first and last name together with a "." in between, and follow it with '@clarusway.com' at the end. Make sure everything is in lowercase.

first_name = "alBerT"
last_name = "eiNSTein"

first_name_capital = first_name.capitalize()
last_name_capital = last_name.capitalize()

# full_name = first_name.capitalize()+" "+last_name.title()
# print(full_name)

# full_name2 = '{} {}'.format(first_name, last_name).title()
# print(full_name2)

# full_name3 = f'{first_name} {last_name}'.title()
# print(full_name3)

# email = first_name_capital.lower()+"."+last_name_capital.lower()+"@clarusway.com"
# print(email)
email2 = f'{first_name}.{last_name}@clarusway.com'.lower()
print(email2)

