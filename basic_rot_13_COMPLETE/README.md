# Basic ROT 13
**Category:** cryptography
> Possibly the easiest ever. plore{TrgFuvsgl13}
---

Untuk menyelesaikan challenge ini kita perlu apa itu enkripsi ROT 13. Kalian bisa [baca disini](http://datagenetics.com/blog/july42015/index.html).

Kita akan gunakan command `tr` untuk mentranslasikan setiap huruf sebanyak 13 kali.
```bash
echo plore{TrgFuvsgl13} | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
```
A-Za-z       akan menjadi ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
N-ZA-Mn-za-m akan menjadi NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm
```

![ROT 13](http://datagenetics.com/blog/july42015/big.png "sumber: datagenetics.com")

Setelah perintah diatas dieksekusi maka kita akan mendapatkan flag yang diinginkan.

flag : `cyber{GetShifty13}`