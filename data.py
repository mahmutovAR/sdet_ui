import rstr


def generate_form_data() -> dict:
    """Returns the generated form data."""
    letters = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f',
               6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
               12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q',
               17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v',
               22: 'w', 23: 'x', 24: 'y', 25: 'z'}
    post_code = rstr.digits(10)
    last_name = rstr.letters(6, 12)
    first_name = ''
    for index in range(0, 9, 2):
        num = int(post_code[index: index+2])
        while num > 25:
            num -= 26
        first_name += letters[num]

    return {'first_name': first_name,
            'last_name': last_name,
            'post_code': post_code}
