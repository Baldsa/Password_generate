import secrets



def create_new(lenght, characters):
    return "".join(secrets.choice(characters) for _ in range(lenght))