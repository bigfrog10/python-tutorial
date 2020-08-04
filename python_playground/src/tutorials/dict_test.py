users = {'mickey':16, 'goofy':50}
users['pluto'] = 40
for user, age in users.items():
    print(user, age)

print(sum(range(4)))

print(users.get('donald', 'not exist'))
# throw KeyError
print(users['donald'])
