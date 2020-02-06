
rsp_dict = {0: 'Rock', 1: 'Fire', 2: 'Scissors', 3: 'Snake', 4: 'Human',
            5: 'Tree', 6: 'Wolf', 7: 'Sponge', 8: 'Paper', 9: 'Air',
            10: 'Water', 11: 'Dragon', 12: 'Devil', 13: 'Lightning',
            14: 'Gun'}

# user = 14
# computer = 7

# user_out = rsp_dict[user]
# comp_out = rsp_dict[computer]

# if ((user + 7) % 15) == computer:
#     print('Win')
# else:
#     print('Lose')

# if computer == user:
#     print('Computer\'s %s ties with User\'s %s' % (comp_out, user_out))
# elif (user + computer) % 15 == (computer + 7) % 15:
#     print('User\'s %s beats Computer\'s %s' % (user_out, comp_out))
#     # print("User:", user, "Computer:", computer, "(user + 7) % 15", (user + 7) % 15)
# else:
#     # print('Computer\'s %s beats User\'s %s' % (comp_out, user_out))
#     # print("User:", user, "Computer:", computer, "(user + 7) % 15", (user + 7) % 15)
#     print('wrong')

# if computer <= ((user + 7) % 15) and computer >= ((user + 1) % 15):
#     print("User Wins")

# try:
#     # user = int(choice)
#     user = 14
#     if user in rsp_dict:
#         user_out = rsp_dict[user]
#         # computer = randint(0, 15)
#         computer = 0
#         comp_out = rsp_dict[computer]
#         if computer == user:
#             outcome = 'Computer\'s %s ties with User\'s %s' % (comp_out, user_out)
#         elif (user + 7) % 15 >= computer and (user + 1) % 15 <= computer:
#             beats = beats_dict[0][1]
#             outcome = 'User\'s %s beats Computer\'s %s' % (user_out, comp_out)
#         else:
#             outcome = 'Computer\'s %s beats User\'s %s' % (comp_out, user_out)
#     else:
#         outcome = 'Error! Incorrect number'
# except ValueError:
#     outcome = 'Error! Incorrect number'
#
# print(outcome)

rsp_dict = {0: 'Rock', 1: 'Fire', 2: 'Scissors', 3: 'Snake', 4: 'Human',
            5: 'Tree', 6: 'Wolf', 7: 'Sponge', 8: 'Paper', 9: 'Air',
            10: 'Water', 11: 'Dragon', 12: 'Devil', 13: 'Lightning',
            14: 'Gun'}

beats_dict = {0: {1: "pounds out", 2: "crushes", 3: "crushes", 4: "crushes", 5: "blocks", 6: "crushes", 7: "crushes"},
              1: {2: "melts", 3: "burns", 4: "burns", 5: "burns", 6: "burns", 7: "burns", 8: "burns"},
              2: {3: "cut", 4: "cut", 5: "carve", 6: "cut", 7: "cut", 8: "cut", 9: "swish through"},
              3: {4: "bites", 5: "nests in", 6: "bites", 7: "swallows", 8: "nests in", 9: "breathes", 10: "drinks"},
              4: {5: "plants", 6: "tames", 7: "cleans with", 8: "writes", 9: "breathes", 10: "drinks", 11: "slays"},
              5: {6: "shelters", 7: "outlives", 8: "becomes", 9: "produces", 10: "drinks", 11: "shelters", 12: "imprisons"},
              6: {7: "chews up", 8: "chews up", 9: "breathes", 10: "drinks", 11: "outruns", 12: "BITES", 13: "outruns"},
              7: {8: "soaks", 9: "USES", 10: "absorbs", 11: "cleanses", 12: "cleanses", 13: "conducts", 14: "cleans"},
              8: {9: "fans", 10: "floats on", 11: "rebukes", 12: "rebukes", 13: "defines", 14: "outlaws", 0: "covers"},
              9: {10: "evaporates", 11: "freezes", 12: "chokes", 13: "creates", 14: "tarnishes", 0: "erodes", 1: "blows out"},
              10: {11: "drowns", 12: "drowns", 13: "conducts", 14: "rusts", 0: "erodes", 1: "puts out", 2: "rusts"},
              11: {12: "commands", 13: "breathes", 14: "immune to", 0: "rests on", 1: "breathes", 2: "immune to", 3: "spawns"},
              12: {13: "casts", 14: "immune to", 0: "hurls", 1: "breathes", 2: "immune to", 3: "eats", 4: "possesses"},
              13: {14: "melts", 0: "splits", 1: "starts", 2: "melts", 3: "strikes", 4: "strikes", 5: "splits"},
              14: {0: "targets", 1: "fires", 2: "outclasses", 3: "shoots", 4: "shoots", 5: "targets", 6: "shoots"}}

extra_dict = {6: {12: "\'s heiney"}, 7: {9: "pockets"}}


for one in beats_dict:
    for two in beats_dict[one]:
        extra = ""
        if (one == 6 and two == 12) or (one == 7 and two == 9):
            extra = extra_dict[one][two]
        print(rsp_dict[one], beats_dict[one][two], rsp_dict[two], extra)

# beats = beats_dict[0].items()  # [0][6]

# print(extra_dict[6][12])
