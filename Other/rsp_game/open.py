import ast

dictionary = open('dictionary.txt', 'r').read()

beats_dict = ast.literal_eval(dictionary)

print(beats_dict[0])
