import random, string, secrets

# some of the named character sets the string library gives us, can be useful for getting WEP keys, etc... string.ascii_letters string.ascii_lowercase string.digits string.octdigits


def gen_custom_pass(length, useUpper, useLower, useNumber, useSpecial, excludeAmbiguous):
    number_Lchars = 1
    number_Uchars = 1
    number_numbers = 1
    number_special = 1
    characters = ''
    password = ''
    excluded = "'\"1lO|`*~.:;,"
    # checks and generate password
    if not 8 <= length <= 100:
        return "Lenght must be between 8 and 100"
    
    if useUpper == 1:
        characters = characters + string.ascii_uppercase
        for index_Upper in range(number_Uchars):
            password = password + secrets.choice(string.ascii_uppercase)
    
    if useLower == 1:
        characters = characters + string.ascii_lowercase
        for index_Lower in range(number_Lchars):
            password = password + secrets.choice(string.ascii_lowercase)
    
    if useNumber == 1:
        characters = characters + string.digits
        for index_digits in range(number_numbers):
            password = password + secrets.choice(string.digits)

    if useSpecial == 1:
        characters = characters + string.punctuation
        for index_special in range(number_special):
            password = password + secrets.choice(string.punctuation)

    if excludeAmbiguous == 1:
        characters  = characters.translate({ord(i): None for i in excluded})
        password = password.translate({ord(i): None for i in excluded})
    
    if not characters:
        return "Please select at least 1 character type."
    
    for index_chars in range(length - len(password)):
        password = password + secrets.choice(characters)
    
    # randomize and then return generated password
    password = randomize_password(password)

    return password


def predefined_pass(_option):
    # use specific character sets when using specific options
    _chars =''
    _length = 0
    _secret = ''

    if _option == 'Memorable':
        _length = 10
        _chars = string.ascii_letters + string.digits
    
    if _option == 'Strong':
        _length = 14
        _chars = string.ascii_letters + string.digits + string.punctuation

    if _option == 'Fortknox':
        _length = 20
        _chars = string.ascii_letters + string.digits + string.punctuation
        #addCharGroups(_chars, string.ascii_letters)
        #addCharGroups(_chars, string.digits)
        #addCharGroups(_chars, string.punctuation)

    return createSecureString(_length, _chars, _secret)



# supporting functions

def randomize_password(to_randomize):
    password_list = list(to_randomize)
    random.shuffle(password_list)
    return "".join(password_list)

def createSecureString(_length, _charSet, _secret):
    for i in range(_length):
        _secret = _secret + secrets.choice(_charSet)
    return _secret
