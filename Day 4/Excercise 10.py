#Excercise: count_chars:

def count_chars(s, to_count='aeiou'):
    # create the output dict
    output = {}
    for one_character in to_count:
        output[one_character] = 0

    # go through the input string
    for one_character in s:
        if one_character in output:     # if one_character is a key in the dict
            output[one_character] += 1  # add 1 to its count

    return output

count_chars('hello out there', 'aeiou')