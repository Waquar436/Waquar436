#first non repeating character
def first_non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating_char('swiss'))
print(first_non_repeating_char('pepper'))
print(first_non_repeating_char('dada'))
print(first_non_repeating_char('annusinha'))
