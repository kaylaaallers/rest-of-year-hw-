import sys

import string





def test(did_pas
    """  Print the result of a test.  """

    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.

    if did_pass:

        msg = "Test at line {0} ok.".format(linenum)

    else:

        msg = ("Test at line {0} FAILED.".format(linenum))

    print(msg)

'''

#ex 3

def count_letters(string,ltr):

    count = 0

    repeats =0

    while repeats < len(string):

        str_index = string.find(ltr,repeats, repeats+1)

        if string.find(ltr,repeats, repeats+1)>=0:

            count+=1

        repeats += 1

     return count

print(count_letters("bananaa","b"))

'''



#ex 4

def count_letters(word,ltr):

    count = 0

    repeats=0

    while repeats < len(word):

        str_index = word.find(ltr,repeats,repeats+1)

        if str_index >= 0:

            count +=1

        repeats +=1



    return count

print(count_letters("banana","a"))

#ex 5

def analyze(str):

    s_without_punct = ""

    for letter in str:

        if letter not in string.punctuation:

            s_without_punct += letter

    mylist=s_without_punct.split()

    count = 0

    for i in mylist:

        if i.find("e")>=0:

            count+=1

    numwords = len(mylist)

    percentage = count / numwords *100



    return 'Your text contains {0} words, of which {1} ({2:.2f}%) contain an "e".'.format(numwords,count,percentage)