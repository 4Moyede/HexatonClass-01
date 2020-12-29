def setEatKimchi(person, time):
    """
    docstring
    """
    raise NotImplementedError

def userData(person, time):
    """
    1. input userData
    2. save userData
    3. return userData
    """
    
    with open("./sample.txt", mode = 'w') as f:
        f.writelines(person, time)

    return person, time

def save_UserData(person, time):
    """
    1. input userData
    2. save userData
        2-1. return userData
        2-2. if error : return error code
    """
    
    try:
        with open("./sample.txt", mode = 'w') as f:
            f.writelines(person, time)
    except Exception as error:
        return error

def load_UserData(path):
    """
    1. input UserData's path
    2. load userData
    """
    with open("./sample.txt", mode = 'r') as f:
        line = f.readlines()

    return line

def sendMessgae(text, isPrivate):
    if isPrivate :
        return 'This is private message. Be careful!!'
    else : 
        return "This is Public Message. Don't care about it"


def sendPrivateMessage(text):
    return 'This is private message. Be careful!!'

def sendPublicMessage(text):
    return "This is Public Message. Don't care about it"

def sendUserData(u, d):
    """
    user_name은 public으로
    user_data은 private으로
    """
    sendPublicMessage(u)
    sendPrivateMessage(d)

def sendUserData(user_name, user_data):
    """
    user_name은 public으로
    user_data은 private으로
    """
    sendPublicMessage(user_name)
    sendPrivateMessage(user_data)
