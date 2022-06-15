
<h1 align="center">
dotfinder
</h1>

<h4 align="center">
dotfinder is a python tool to find subdomains!
</h4>

<p align="center">
  • <a href="#installation">Installation</a>
  • <a href="#usage">Usage</a>
  • <a href="#commands">Commands</a>
  • <a href="#features">Features</a>
</p>

---

# Installation

Run this to install:
 
```sh
$ git clone https://github.com/Miguel-Galdin0/dotfinder.git
```

# Usage
 
```sh
$ python3 dotfinder.py [-d DOMAIN] [opitional commands]
```
You can use `url` or <a href="#features">pipe</a> to enumerate.

Exemple:

<img src="/images/exemple.png" alt="dotfinder" width="700px"></a>


# Commands

Use this if you need help with commands:

```sh
$ python3 dotfinder.py -h
```

# Features

| Feature  | Descripition             |
| -------- | ------------------------ |
| Pipeline | - From I/O module (`echo "hackerone.com" | python3 dotfinder.py -d pipe`) |
| Silet mode | - Show only the subdomains with flags `-s` or `--silet` (`python3 dotfinder.py -d hackerone.com -s`) |
| Auto HTTP remove | - If you use a url with `http://` or `https://`, the tool automatically remove this.|
