# 0 - Dynamite

rsp_dict = {0: 'Dynamite', 1: 'Tornado', 2: 'Quicksand', 3: 'Pit', 4: 'Chain',
            5: 'Gun', 6: 'Law', 7: 'Whip', 8: 'Sword', 9: 'Rock',
            10: 'Death', 11: 'Wall', 12: 'Sun', 13: 'Camera',
            14: 'Fire', 15: 'Chainsaw', 16: 'School', 17: 'Scissors',
            18: 'Poison', 19: 'Cage', 20: 'Axe', 21: 'Peace', 22: 'Computer',
            23: 'Castle', 24: 'Snake', 25: 'Blood', 26: 'Porcupine',
            27: 'Vulture', 28: 'Monkey', 29: 'King', 30: 'Queen', 31: 'Prince',
            32: 'Princess', 33: 'Police', 34: 'Woman', 35: 'Baby', 36: 'Man',
            37: 'Home', 38: 'Train', 39: 'Car', 40: 'Noise', 41: 'Bicycle',
            42: 'Tree', 43: 'Turnip', 44: 'Duck', 45: 'Wolf', 46: 'Cat',
            47: 'Bird', 48: 'Fish', 49: 'Spider', 50: 'Cockroach', 51: 'Brain',
            52: 'Community', 53: 'Cross', 54: 'Money', 55: 'Vampire',
            56: 'Sponge', 57: 'Church', 58: 'Butter', 59: 'Book', 60: 'Paper',
            61: 'Cloud', 62: 'Aeroplane', 63: 'Moon', 64: 'Grass', 65: 'Film',
            66: 'Toilet', 67: 'Air', 68: 'Planet', 69: 'Guitar', 70: 'Bowl',
            71: 'Cup', 72: 'Beer', 73: 'Rain', 74: 'Water', 75: 'T.V.',
            76: 'Rainbow', 77: 'U.F.O.', 78: 'Alien', 79: 'Prayer',
            80: 'Mountain', 81: 'Satan', 82: 'Dragon', 83: 'Diamond',
            84: 'Platinum', 85: 'Gold', 86: 'Devil', 87: 'Fence',
            88: 'Video Game', 89: 'Maths', 90: 'Robot', 91: 'Heart',
            92: 'Electricity', 93: 'Lightning', 94: 'Medusa', 95: 'Power',
            96: 'Laser', 97: 'Nuke', 98: 'Sky', 99: 'Tank', 100: 'Helicopter'}

death = ['KNOWS NO' ,
'CLAIMS' ,
'RUINS' ,
'COOLS' ,
'DISMANTLES' ,
'SADDENS' ,
'NOT CAUSED BY' ,
'(S ALL LIFE)' ,
'INSIDE' ,
'CARRIES' ,
'RESTs IN' ,
'CRASHES' ,
'CRUMBLES' ,
'CLAIMS' ,
'COOLS' ,
'CLAIMS' ,
'FEEDS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'SADDENS' ,
'STOPS' ,
'CRASHES' ,
'RATTLE' ,
'CRASHES' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'CLAIMS' ,
'SADDENS' ,
'ON' ,
'COSTS' ,
'ELUDES' ,
'DRIES' ,
'SADDENS' ,
'SPOILS' ,
'CRUMBLES' ,
'CRUMBLES']

# main = 10
# i = 11
#
# dictionary = {}
#
# for item in death:
#     dictionary[i] = item.lower()
#     i += 1
#
# print(dictionary)

# for item in dictionary:
#     print(rsp_dict[main], dictionary[item], rsp_dict[item])

weapon = 5

to_print = {6: 'breaks', 7: 'outclasses', 8: 'outclasses', 9: 'targets', 10: 'causes', 11: 'targets', 12: 'shoots at', 13: 'shoots at', 14: 'fires', 15: 'outclasses', 16: 'closes', 17: 'outclasses', 18: 'deadlier than', 19: 'shoots through', 20: 'outclasses', 21: 'disturbs', 22: 'shoots', 23: 'fires into', 24: 'shoots', 25: 'spills', 26: 'shoots', 27: 'shoots', 28: 'shoots', 29: 'shoots', 30: 'shoots', 31: 'shoots', 32: 'shoots', 33: 'shoots', 34: 'shoots', 35: 'shoots', 36: 'shoots', 37: 'protects', 38: 'holds up', 39: 'hijacks', 40: 'makes', 41: 'shoots bicycle', 42: 'targets', 43: 'blasts apart', 44: 'shoots', 45: 'shoots', 46: 'shoots', 47: 'shoots', 48: 'shoots', 49: 'shoots', 50: 'shoots', 51: 'splatters', 52: 'threatens', 53: '(hair)', 54: 'robs', 55: 'shoots (with a silver bullet)'}

for key in to_print:
    print(rsp_dict[weapon], to_print[key], rsp_dict[key])
