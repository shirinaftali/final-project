"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""

#import pytest

def no_duplicates(a_string):
    new_a_string1 = a_string.replace(" ","")
    new_a_string = sorted(new_a_string1)
    ni = len(new_a_string)
    i = 0
    for i in range(0, ni-8):
        if new_a_string[i] == new_a_string[i+1]:
            new_a_string.pop(i)
            ##print(new_a_string)
        i+=1

    print(''.join(new_a_string))


#####################################################
def reversed_words(a_string):

    new1= a_string.split()
    j = len(new1)
    new_a_string = []
    i = 1
    for i in range(0,j):
        x=j-i-1
        new_a_string.append(new1[x])
        i+=1
    j+=1
    print(new_a_string)


##################################################################
def four_char_strings(a_string):
    new_a_string = []
    i=0
    for i in range(i, len(a_string)-4, 4):
        x=i+4
        z = a_string[i:x] + " "
        new_a_string.append(z)
    print(new_a_string)



#################################

def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

""""
def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
"""


s_word = ("monty pythons flying circus")
no_duplicates(s_word)
reversed_words(s_word)
four_char_strings(s_word)


