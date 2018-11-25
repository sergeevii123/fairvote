from boa.interop.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.interop.Neo.Storage import Get, Put, GetContext
from boa.builtins import concat
from kyc import *
from txio import *

OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'
ctx = GetContext()

def Main(operation, args):

    if operation == 'deploy':
        return deploy()

    if operation == 'add_users':
        print("Running Verification!")
        is_owner = CheckWitness(OWNER)

        if is_owner:
            print("Is Owner!")
            return add_users(args)

        print("Not Owner")
        return False
    
    if operation == 'check_user':
        user = args[0]
        return check_user(user)

    if operation == 'current_vote':
        user = args[0]
        return current_vote(user)


def add_users(users):
    ok_count = 0
    for user in users:
        msg = concat("Adding user: ", user)
        Notify(msg)
        Put(ctx, user, "blank_vote")
        current_user_number = Get(ctx, "all_users")
        Put(ctx, "all_users", current_user_number+1)
        res = kyc_register(ctx, user)
        if res:
            ok_count += 1

    Notify(concat("Added users ", ok_count))
    return ok_count


def current_vote(user):
    kyc_status = sender_is_in_DAO(ctx)
    if kyc_status:
        vote = Get(ctx, user)
        Notify(vote)
        print("current vote", vote)
        return True
    return False


def check_user(user):
    msg = concat("Checking user: ", user)
    Notify(msg)

    vote = Get(ctx, user)
    if len(vote) > 0:
        Notify("User is not in DAO")
        return False

    kyc_status = sender_is_in_DAO(ctx)
    print("User is in DAO kyc ", kyc_status)
    return user


def deploy():
    if not CheckWitness(OWNER):
        print("Must be owner to deploy")
        return False

    Put(ctx, 'initialized', 1)
    Put(ctx, OWNER, "blank_vote")
    Put(ctx, "all_users", 1)
    
    return True