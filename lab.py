## p1


# - Create a list named `students` containing some student names (strings).
students = ['s1','s2','s3']
# - Print out the second student's name.
print(students[1])
# - Print out the last student's name.
print(students[-1])


#### Exercise 2

# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
foods = ('apple', 'banana', 'orange','pepper')
# - Use a `for` loop to print out the string "_food goes here_ is a good food".
for food in foods:
  print(f"{food} is a good food")
# #### Exercise 3

# - Using a `for` loop, print just the last two food strings from `foods`.
for idx, food in enumerate(foods):
  if (idx > len(foods)-3) :
    print(food)

# #### Exercise 4

# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
# - Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"
home_town = {
  'city': 'SD',
  'state': 'CA',
  'population': '13,000,000'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# #### Exercise 5
# - Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"
for key, val in home_town.items():
  print(f"{key}: {val}")

# #### Exercise 6

# - Create an empty list named `cohort`.
# - Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:
cohort = []
students = ['Ollo', 'Jennifer', 'Hailey', 'Matt']
fave_foods = ['british food', 'asian food', 'asian food', 'american food']
for idx, student in enumerate(students):
  fav_food = {
    'student': student,
    'fav_food': fave_foods[idx]
  }
  cohort.append(fav_food)

print(cohort)
# 	```python
# 	{
# 	  'student': 'Tina',
# 	  'fav_food' 'Cheeseburger'
# 	}
# 	```
# - Iterate over `cohort` printing out each element.

# #### Exercise 7

# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing
#strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over `awesome_students` printing out each string.

awesome_students = [f"{student} is awesome" for student in students]
print(awesome_students)

# #### Exercise 8

# - Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.


a_foods = [food for food in foods if 'a' in food]
print(a_foods)
