# Reversal of Fortune
**Category:** miscellaneous
```
Our team of agents have been tracking a hacker that sends cryptic messages to other hackers about what he's doing. We intercepted the below message he sent recently, can you figure out what it says? He mentions his hacker name in it, that's the code you need. .nac uoy fi tIe$reveRpilF eldnah ym gnisu em egassem ,avaj yllacificeps ,gnidoc emos htiw pleh deen I ,deifitnedi tegrat txeN
```
---

Di challenge ini kita diminta untuk memasukkan nama hacker yang terdapat di dalam pesan yang di "Enkripsi".

Pada kalimat terakhir terdapat pesan yang cukup aneh, jika diperhatikan setiap kata adalah kata yang dibalik posisinya. Untuk menyelesaikan soal ini bisa menggunakan bahasa pemrograman Python dengan teknik substring. [Baca disini](https://www.dotnetperls.com/substring-python)

```python
soal  = ".nac uoy fi tIe$reveRpilF eldnah ym gnisu em egassem ,avaj yllacificeps ,gnidoc emos htiw pleh deen I ,deifitnedi tegrat txeN"
hasil = soal[::-1]
print(hasil)
```

Pada bagian akhir kalimat terdapat nama hacker yang kita cari, dan itu adalah flag yang kita cari.

flag : `FlipRever$eIt`
