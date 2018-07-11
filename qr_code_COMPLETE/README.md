# QR Code
**Category:** miscellaneous

> Do you remember something known as QR Code? Simple. Here for you : 
> https://mega.nz/#!Ej4n3RSI!8mbiqg3kosk93qJCP-DBxIilHH2rf7iIVY-kpwyrx-0
---

![QR Code CTFLearn v1](./qrcode.39907201.png "QR Code")

Untuk menyelesaikan challenge QR Code ini kita perlu membaca pesan yang tersimpan di dalamnya. Kita bisa gunakan [QR Scanner online](https://webqr.com/index.html).

Kita mulai dengan scan QR Code dan simpan hasilnya kedalam file hasil_scan.txt
```bash
echo c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI= > hasil_scan.txt
```

Bila diperhatikan pesan ini adalah bentuk dari **Base64 Encoding** ([Baca disini](https://en.wikipedia.org/wiki/Base64)) karena terdapat simbol "sama dengan" (`=`) di akhir. Maka kita perlu melakukan _decoding_ terhadap pesan ini.
```bash
cat hasil_scan.txt | base64 -d
```

> synt vf : a0\_obql\_s0etrg\_de\_pbqr

Setelah di-_decode_ kita mendapat pesan yang sulit dibaca, namun pesan ini sebenarnya mengandung. Bisa dilihat dari karakteristik pesan tersebut bisa jadi merupakan _ciphertext_ dari enkripsi **ROT13** ([Baca disini](http://datagenetics.com/blog/july42015/index.html)).

Mari kita coba dekripsi _ciphertext_ ini dengan ROT13.

```bash
cat hasil_scan.txt | base64 -d | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
* `tr`: _translate_ karakter sesuai dengan bentuk yang kita inginkan. Baca keterangan _command_ ini dengan `man tr`.
* `A-Za-z`: bentuk pertama (`ABC...XYZabc....xyz`)
* `N-ZA-Mn-za-m`: di-_translate_ menjadi bentuk kedua (`NOP...XYZABC...KLMnop...xyzabc...klm`)

![ROT13 Encryption](http://datagenetics.com/blog/july42015/big.png "sumber: datagenetics.com")

flag : `n0_body_f0rget_qr_code`