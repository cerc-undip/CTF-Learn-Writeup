#!/bin/bash

soal="d2FvLCBhbG1vc3QgdGhlcmUNClpHOXVKM1FnZDI5eWNua3NJSE52YjI0TkNscHRlR2hhTTNSd1pFWTVjR014T1hwaU1UbHNXVmhPTldaUlBUMD0="

echo $soal | base64 -d | grep = | base64 -d | grep = | base64 -d
