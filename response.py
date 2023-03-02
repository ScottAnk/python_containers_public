# exercise 1

students = ['heather', 'quentin', 'akihiko', 'scott']
print(students[1:4:2])

# exercise 2

foods = ('spaghetti', 'toast', 'escargot', 'kimchi')
for food in foods:
    print(f"{food} is a good food")

# exercise 3

for food in foods[2:]:
    print(f"{food} is a good food")

# exercise 4

home_town = {
    'city': 'Amesbury',
    'state': 'Massachusetts',
    'population': 25000
}
print(
    f'I was bord in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# exercise 5

for key, value in home_town.items():
    print(f"{key} = {value}")

# exercise 6

cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })
    # print(cohort[-1])

for student in cohort:
    print(student)

# exercise 7

awesome_students = [f"{student} is awesome!" for student in students]
for student in awesome_students:
    print(student)

# exercise 8

for a_foods in [food for food in foods if 'a' in food]:
    print(a_foods)
