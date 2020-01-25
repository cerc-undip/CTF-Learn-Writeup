# Binwalk
**Category:** forensic
```
https://mega.nz/#!4UEnAZKT!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY
```
---

After you download from the above link, we go to the directory where it has been downloaded.
```
binwalk -D "png image:png" PurpleThing.jpeg
```
This will just extract the hidden zip files and contents which has the flag.
```cd _PurpleThing.jpeg.extracted
```
You will find the flag there.
flag : `ABCTF{B1nw4lk_is_us3ful}`
