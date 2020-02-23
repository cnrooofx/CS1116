import ast

dictionary = open('dictionary.txt', 'r').read()

beats_dict = ast.literal_eval(dictionary)

print(beats_dict[0])


dictionary = {0: {1: 'hi'}}

print(dictionary[0][1])
