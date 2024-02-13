def reverseWord(sentence):
    words = sentence.split()
    rev = words[::-1]

    return ' ' . join(rev)

sentence = input("Input your sentence : ")

print('Reversed sentence : ' + reverseWord(sentence))