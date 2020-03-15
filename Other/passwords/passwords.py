
passwords = open('eff_wordlist.txt', 'r')
out = open('wordlist.txt', 'w')

dictionary = {}

for line in passwords.readlines():
    to_dict = line.strip('\n').split('\t')
    dictionary[to_dict[0]] = to_dict[1]


out.write(str(dictionary))

out.close()
passwords.close()
