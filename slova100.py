import os

def words(fname="input.txt", N=100):
    myfile = open(fname, "r", 1)
    word_dict = {}
    current_line = myfile.readline()
    while current_line:
        #getting words in line
        words_in_line = current_line.split()

        #counting word w
        for w in words_in_line:
            if w in word_dict:
                word_dict[w] = word_dict[w] + 1
            else:
                word_dict[w] = 1
        #go to next line until EOF
        current_line = myfile.readline()

    #we don't want to word_dict.pop() more times then len(word_dict)
    if len(word_dict) < N:
        return word_dict

    #just some bunch of shitcode
    return_dict = {}
    for i in range(0, N):
        m = word_dict.popitem()
        mword = m[0]
        mcount = m[1]
        word_dict[mword] = mcount
        for word in word_dict.keys():
            if word_dict[word] > mcount:
                mword = word
                mcount = word_dict[word]
        word_dict.pop(mword)
        return_dict[mword] = mcount
    return return_dict