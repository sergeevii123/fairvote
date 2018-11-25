from neocore.Cryptography.Crypto import Crypto
pubkey_hex = '031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf98'
pubkey_hex_for_addr = '21' + pubkey_hex + 'ac'
script_hash = Crypto.ToScriptHash(pubkey_hex_for_addr, unhex=True)
print(script_hash.Data)