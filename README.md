# Get Contract Address's Tx Hash and Block Hash


This is an example of web3 "how to get Tx hash and Block hash of a contract addres". Currently web3.py doesn't provide a method that allow us to get these information. The way than I found it was checking in blocks if contract is already created.


### Tech

This example was devdeloped with ```python 3.6.5``` and used ```web3.py```

you can get your own node in https://infura.io/


### Installation

Install the dependencies and run

```sh
$ cd <project directory>
$ pip install web3
$ python main.py --host <URL Node> <Contract Address>
```


### Development

Want to contribute? Great! Clone this repository and enjoy
