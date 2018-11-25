# fairvote

Solution for https://2018.hackjunction.com/challenges/dao-voting

```
build contr/voting.py
import contract contr/voting.avm 0710 05 True False False
contract search vote
testinvoke 0x97d87b287c82cfc0b74bd7e67bbe9e1cbbfd090d deploy []
testinvoke 0x97d87b287c82cfc0b74bd7e67bbe9e1cbbfd090d add_users ['\x12`}\xdf\xd1\x08\x84}\xad{\x91\r"\xc0@\xe5\x10U3\x84', 's\x9a`\xf0\xado\xf2Y\xc5\x8dcn\x03/\x17\xa1%\xa5\xa8\xd8']

testinvoke 0x97d87b287c82cfc0b74bd7e67bbe9e1cbbfd090d current_vote ['\x12`}\xdf\xd1\x08\x84}\xad{\x91\r"\xc0@\xe5\x10U3\x84']
testinvoke 0x97d87b287c82cfc0b74bd7e67bbe9e1cbbfd090d current_vote ['s\x9a`\xf0\xado\xf2Y\xc5\x8dcn\x03/\x17\xa1%\xa5\xa8\xd8']
```
