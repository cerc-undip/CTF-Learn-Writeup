# Crack Me
**Category:** cryptography
> If A=Z, B=Y..., then what is:
> XGU{Rmhvxfiv=Vzhb}
---

Challenge Cryptaz ini sudah memberikan algoritma yang dipakai untuk merahasiakan pesannya. Jika kita lihat lagi bahwa algoritma yang dipakai ini adalah algoritma yang pernah dipakai pada saat kita mengikuti Pramuka, yaitu sandi A-Z. Keren kan? Wkwkwk

![Sandi A-Z](https://aboutpramuka.files.wordpress.com/2015/12/sandi-abjad-az.jpg "sumber: aboutpramuka.wordpress.com")

Untuk menyelesaikan challenge ini kita cukup mentranslasikannya saja dengan perintah `tr`. Jika ingin lebih paham bisa baca manualnya `man tr`.
```bash
echo XGU{Rmhvxfiv=Vzhb} | tr 'A-Za-z' 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
```
* Penulisan huruf dari A sampai dengan Z dan a sampai dengan z bisa ditulis dengan `A-Za-z`.
* Namun untuk sebaliknya tidak bisa dilakukan, maka ditulis secara manual.

flag : `CTF{Insecure=Easy}`