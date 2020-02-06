
user = 13
computer = 4

# if ((user + 7) % 15) == computer:
#     print('Win')
# else:
#     print('Lose')

if computer == user:
    outcome = 'Computer\'s %s ties with User\'s %s' % (computer, user)
elif (user + 7) % 15 <= computer:
    outcome = 'User\'s %s beats Computer\'s %s' % (user, computer)
else:
    outcome = 'Computer\'s %s beats User\'s %s' % (computer, user)

# print(outcome)
print((14+7) % 15)
