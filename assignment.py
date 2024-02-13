sentence = input("Input your sentence : ")

words = sentence.split()
rev = words[::-1]

print('Reversed sentence : ' + ' ' . join(rev))