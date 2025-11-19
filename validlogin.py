def login(email, password):
    passwordnumbers = 0
    passwordupper = 0
    if "@" not in email: 
        return "Invalid email (No @ included)."
    if not isinstance(email, str):
        return "Invalid email (Not a string)."
    if not len(password) >= 8:
        return "Invalid Password (Not 8 characters)."
    if not isinstance(password, str):
        return "Invalid Password (Not a string)."
    for i in range (len(password)):
        if password[i].isdigit():
            passwordnumbers += 1
        if password[i].isupper():
            passwordupper += 1
    if passwordnumbers < 1:
        return "Invalid Password (Missing a number)."
    if passwordupper < 1:
        return "Invalid Password (Missing an uppercase letter)."
    return (f"Email: {email}, Password: {password}")
print(login("natural@gmail.com", "Helloi3ii"))
    