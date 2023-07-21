def solution(my_string):
    vowel='aeiou'
    for i in my_string:
        if i in vowel:
            my_string = my_string.replace(i, '')
    return my_string