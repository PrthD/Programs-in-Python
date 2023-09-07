def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid".
    """
    if " " in password or  "#" in password or "@" in password or len(password) < 8:
        return("Invalid")
    else:
        List = []
        for i in password:
            if i.islower():
                List.append("L")
            elif i.isupper():
                List.append("U")
            elif i.isnumeric():
                List.append("N")
            elif (i in "!-$%&'()*+,./:;<=>?_[]^`{|}~"):
                List.append("C")
        if ("L" in List) and ("U" in List) and ("N" in List) and ("C" in List):
            return("Secure")
        else:
            return("Insecure")
    pass


def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n.
    """
    import random
    import string
    characters = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    password = []
    if n < 8:
        return
    else:
        for i in range(n):
            password.append(i)
        password[0] = random.choice(string.ascii_uppercase)
        password[1] = random.choice(string.ascii_lowercase)
        password[2] = random.choice(characters)
        password[3] = str(random.randint(1,9))
        for i in range(4,n):
            choose = random.randint(0,3)
            if choose == 0:
                password[i] = random.choice(string.ascii_uppercase)
            elif choose == 1:
                password[i] = random.choice(string.ascii_lowercase)
            elif choose == 2:
                password[i] = random.choice(characters)
            elif choose == 3:
                password[i] = str(random.randint(1,9))
        random.shuffle(password)
        password_str = ''.join(password)
        return password_str

    pass

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    print(generate(1))
    print(generate(10))
    print(generate(20))
    pass