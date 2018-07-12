# Esrom Leumas
**Category:** cryptography
> I got a message from Esrom Leumas:
> ..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ... .
> The flag has format: flag{FourWordsInCamelCase}
---

Kata kunci untuk menyelesaikan challenge ini adalah pada judulnya "Esrom Leumas". Jika dibalik, kata ini berarti "Samuel Morse". Oke, kita kembali lagi ke masa Pramuka untuk menyelesaikan challenge ini.

Kita bisa gunakan bahasa pemrograman Python atau jika ingin cepat bisa gunakan [Morse Code Translator Online](https://morsecode.scphillips.com/translator.html?utm_source=hootsuite).

Mari kita buat file `script.py` dan ubah menjadi _executable_, kemudian buka file tersebut.
```bash
touch script.py
chmod +x script.py
```

```python
#!/usr/bin/python3
soal = "..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ... ."

hasil = soal.split(" ")
print(hasil)
```

Dengan program diatas, kita masukkan tiap kode yang dipisahkan dengan spasi kedalam variabel `hasil`.

Pasangan antara kode morse dengan huruf kita gunakan tipe data `dictionary` dari Python.
```python
#!/usr/bin/python3
soal = "..-. .-.. .- --. ... .- -- ..- . .-.. -- --- .-. ... . .. ... -.-. --- --- .-.. -... -.-- - .... . .-- .- -.-- .. .-.. .. -.- . -.-. .... . . ... ."

sandi = {
  ".-": "A",
  "-...": "B",
  "-.-.": "C",
  "-..": "D",
  ".": "E",
  "..-.": "F",
  "--.": "G",
  "....": "H",
  "..": "I",
  ".---": "J",
  "-.-": "K",
  ".-..": "L",
  "--": "M",
  "-.": "N",
  "---": "O",
  ".--.": "P",
  "--.-": "Q",
  ".-.": "R",
  "...": "S",
  "-": "T",
  "..-": "U",
  "...-": "V",
  ".--": "W",
  "-..-": "X",
  "-.--": "Y",
  "--..": "Z"
}

hasil = soal.split(" ")

decoded = []
for j in range(len(hasil)):
  decoded.append(sandi[hasil[j]])

print("".join(decode))
```

Program diatas akan otomatis mengakses setiap kode di variabel `hasil` dan mencocokkan dengan _dictionary_ di variabel `sandi`. Hasil dari pencocokkan tersebut dimasukkan kedalam list/array decoded. Terakhir kita tampilkan hasil penggabungan kata di dalam variabel `decoded`.

Perhatikan bahwa format flag-nya adalah **flag{FourWordsInCamelCase}**.

flag : `flag{SamuelMorseIsCool}`