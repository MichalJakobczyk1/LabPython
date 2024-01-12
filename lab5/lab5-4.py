import random
import string

def gen_pass(length, min_letters=1, min_digits=1):
    for _ in range(length - min_letters - min_digits):
        yield random.choice(string.ascii_letters)

    for _ in range(min_letters):
        yield random.choice(string.ascii_lowercase)

    for _ in range(min_digits):
        yield random.choice(string.digits)

password = gen_pass(length=8, min_letters=2, min_digits=2)

for _ in range(5):
    generated_password = ''.join(password)
    random.shuffle(generated_password)
    print(''.join(generated_password))