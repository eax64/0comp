# 0comp
This program let you compress file without loss with an infinite compression rate.

```
$> dd if=/dev/zero of=original bs=1M count=1
$> du -h original 
1.0M  original
$>
$> ./0comp.py -c original 
The compressed file has been saved in the file: AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg==
$> du -h AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg==
0  AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg==
$>
$> ./0comp.py -d AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg== > decompressed
$> du -h decompressed
1.0M  decompressed
$> md5sum original decompressed
b6d81b360a5672d80c27430f39153e2c  original
b6d81b360a5672d80c27430f39153e2c  decompressed
```


[![asciicast](https://asciinema.org/a/bu6pgxo6xhc83d34lpep23o80.png)](https://asciinema.org/a/bu6pgxo6xhc83d34lpep23o80)

You can also compress bigger file with the -b option:

```
$> dd if=/dev/urandom of=original bs=1M count=1
$> du -h original 
1.0M  original
$>
$> ./0comp.py -b compressed -c original 
The compressed file has been saved in the file: compressed
$> du -hc compressed/*
0  compressed/...
0  compressed/...
0  total
$>
$> ./0comp.py -d compressed > decompressed
$> md5sum original decompressed 
79619e28282cab77534b46b280122387  original
79619e28282cab77534b46b280122387  decompressed
```
