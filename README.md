# cernet-hawk

[![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/)

A port scan project.

# Installation

### Requirements

* nmap
* zmap
* rabbitmq

### Installation on Ubuntu

```shell
git clone https://github.com/sea0breeze/cernet-hawk.git
chmod +x cli/install.sh
chmod +x cli/iptables.sh
chmod +x do.sh

./cli/iptables.sh
./cli/install.sh
```

# Usage

```shell
./do.sh startall
```
