def authentication(fn):
    def check_inner(*args):
        if args[0]["valid"]:
            return fn(*args)
        else:
            return print("User not valid")

    return check_inner


user1 = {"name": "Sorana", "valid": True}


@authentication
def message_friends(user):
    print("message has been sent")


message_friends(user1)
