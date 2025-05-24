# Pexy
a simple port scanner written in python by ***Exyth***.
## 📌 How to use ?
First of all, pexy uses **arguments** to work, which means to run it you'll have to run it from the **terminal/cmd**

*** 🧭 Step by step***
- Open terminal/cmd and travel to the directory that pexy is in.
- Run this >> python pexy.py -h
- To simplify it heres a basic way to run the tool >> python pexy.py -t 127.0.0.1

  ## 📚 Arguments explained
- -t/--target          : Set the target                                                                                                                     **>>** Example: python pexy.py -t 127.0.0.1
- -p1/--startport      : Set the starting port                                                                                                              **>>** Example: python pexy.py -t 127.0.0.1 -p1 10
- -p2/--endport        : Set the ending port                                                                                                                **>>** Example: python pexy.py -t 127.0.0.1 -p2 1024
- -p/--sports          : Set your own list of ports (!!!comma seperated!!!)                                                                                 **>>** Example: python pexy.py -t 127.0.0.1 -p 24,433,92,13,21
- -tm/--timeout        : Set timeout duration                                                                                                               **>>** Example: python pexy.py -t 127.0.0.1 -tm 5
- -th/--threads        : Set number of threads (controls how fast the scanning runs) **BEWARE**: if you have a weak pc do not edit this                     **>>** Example: python pexy.py -t 127.0.0.1 -th 1000
- -sp/--showports      : Show ports while scanning even if they are closed                                                                                  **>>** Example: python pexy.py -t 127.0.0.1 -sp
- -os/--osdetection    : Toggles OS detection                                                                                                               **>>** Example: python pexy.py -t 127.0.0.1 -os
- -h/--help            : Shows a simple help page                                                                                                           **>>** Example: python pexy.py -h
