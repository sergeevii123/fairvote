from boa.interop.Neo.Blockchain import GetHeight
from boa.interop.Neo.Runtime import CheckWitness
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.Storage import Get, Put
from boa.builtins import concat
from txio import *

OnKYCRegister = RegisterAction('kyc_registration', 'address')
KYC_KEY = b'kyc_ok'
OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'


def kyc_register(ctx, address):
    kyc_storage_key = concat(KYC_KEY, address)
    Put(ctx, kyc_storage_key)
    OnKYCRegister(address)
    return True
    


def sender_is_in_DAO(ctx):
    attachments = get_asset_attachments() 
    print("user", attachments[1])
    if not get_kyc_status(ctx, attachments[1]):
        return False
    return True


def get_kyc_status(ctx, address):
    print("checking kyc status")
    kyc_storage_key = concat(KYC_KEY, address)

    return Get(ctx, kyc_storage_key)
