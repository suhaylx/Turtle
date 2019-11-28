dicts = {
'b' : 1,
'c': 2,
'key' : "Password"
}
#print(dicts['key'])


my_list_of_hero = [{
'b' : [1,45,2],
'c': 2,
'key' : "Password"
}, 
{
'boss_level' : [1,2,5,9,10],
'health':2,
'Name' : "Password"
}
]


print ("print your hero completed boss level ",my_list_of_hero[1]['boss_level'][0])

user = dict(name = "Suhaylx")
print(user)

print(user.get('bla', "no such keeey boo "))