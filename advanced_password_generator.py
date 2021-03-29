import random
import string

class CommonMethods:
    def __init__(self):
        self.lower_character = []
        self.upper_character = []
        self.list_numbers = []
        self.pun_character = []

    def lower_char(self):
        # Generate lower case characters and return
        for i in string.ascii_lowercase:
            self.lower_character.append(i)
        return self.lower_character

    def upper_char(self):
        # Generate upper case characters and return
        for i in string.ascii_uppercase:
            self.upper_character.append(i)
        return self.upper_character

    def list_num(self):
        # Generate numbers from 0..9 and return
        for i in string.digits:
            self.list_numbers.append(str(i))
        return self.list_numbers

    def pun_char(self):
        # Generate punctuation and return
        for i in string.punctuation:
            self.pun_character.append(str(i))
        return self.pun_character

class AdvancedPasswordGenerator:
    obj = CommonMethods()
    password_len = int(input('Password Length ?'))

    new_pass = []
    counter = 1

    l_characters = obj.lower_char()
    u_characters = obj.upper_char()
    l_numbers = obj.list_num()
    p_characters = obj.pun_char()

    while counter <= (password_len) / 4 + 2:
        random_counter = random.randrange(0, 10)
        new_pass.append(l_numbers[random.randrange(0, 10)])
        new_pass.append(u_characters[random.randrange(0, 26)])
        new_pass.append(p_characters[random_counter])
        new_pass.append(l_characters[random.randrange(0, 10)])
        # new_pass.append(lower_character[random.randrange(0, 26)])
        counter += 1
    password = "".join(new_pass)
    password = password[0:password_len]
    print(f'Generated Password length is {len(password)} :\n{password}')

run_password_generator = AdvancedPasswordGenerator()
