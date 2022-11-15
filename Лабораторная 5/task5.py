import random
import string
string.ascii_uppercase
string.ascii_lowercase
string.digits

def get_random_password() -> str:
    len
    password = (string.ascii_uppercase + string.ascii_lowercase +  string.digits)
    new_random_password = random.sample(password, k = 5)
    return new_random_password

new_random_password = get_random_password()
print(get_random_password())
