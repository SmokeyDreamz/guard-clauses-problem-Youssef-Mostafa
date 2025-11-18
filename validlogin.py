def login(email, password):
    if "@" not in email: 
        return "Your email is invalid"
    return (f"Email: {email}, Password: {password}")
print(login("natural@gmail.com", "hello"))
    