pget - MULTITHREAD IMPLEMENTATION BRANCH
======

Python program that emulates the wget linux command. This program allows 
continue or resume a download where it failed or was interrupted.

This program is not intended to be used in a production system. It aims to show how resuming downloads works.
## Installation and Getting Started
* requirements
* clone this repo
* usage

### Requirements
* Python 2.7 is required to run the code

### Clone the repo
```bash
$ git clone https://github.com/imarban/pget.git
$ cd pget
```

### Basic usage
```bash
$ python client.py <url> 
```

Replace <url> for the actual url you want to download

### Usage

The program accept some parameters at the invoking time 

* -c --continue If you are trying to continue a download which was interrupted you need to set this flag. If you don't
use this flag the previous download attempts for the same resource are going to be deleted.
* -o --outfile If this argument is passed, the name of the file where the download content is written is going to be
changed. If this parameter is absent the file name will be extracted from the url last part.
* -v --verbose. It sets the logger level to DEBUG for seeing more information.

```bash
$ python client.py <url> -c -o <filename.extension> -v 
```

### Resources

The next are some resources that were useful at the time I was writing this program: 

* http://www.thinkbroadband.com/download.html Download test files
* http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html Range HTTP header
* https://docs.python.org/2/library/urllib2.html How to make a request in HTTP with Python