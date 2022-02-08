# Jenkinsploit

## Overview

Jenkinsploit is an attack and exploitation toolkit tailored toward Jenkins. It was written to provide a single solution for offensive security professionals to quickly map, enumerate, and attack misconfigured Jenkins instances.
Currently, only Linux targets are supported. Windows-specific payloads, TTP's, and obfuscation are currently being developed.

## Features

Jenkinsploit includes a broad list of features, including:

 - Fingerprinting of Jenkins software stack and version
 - Privilege level and access evaluation
 - Authentication using user credentials or a logged-in user's cookie for session hijacking
 - Exploits for multiple widely-known vulnerabilities
 - Capable of enumerating users, nodes, jobs, plugins, and more
 - On-demand creation and deletion of user accounts
 - Credential dumping and decryption
 - Multiple Groovy code execution methods
 - Automated funcionality to access and exfil sesntive files and secrets from filesystem of target instance
 - Security warning detection and vulnerability parsing
 - Jenkins outdated version detection

## Installation

    git clone https://github.com/k0fin/jenkinsploit.git
    cd jenkinsploit
    python3 -m pip install -r requirements.txt
    sudo python3 ./setup.py install

    jenkinsploit --help

## Usage

* Authentication
* Discovery
* Detections
* Attacks
* Utilities

## To Do

* Password spraying
* log4j vulnerability detection for installed plugins
* include current class methods as individual modules for extensibility and customization
* Windows-specific payloads and support
* Groovy payload generation and obfuscation
* Job builder code execution fixes
* Added support for full CI/CD pipeline environments
* Node mapping and multi-instance takeover/command and control
* Payloads for persistence methods



## Credits & References

The following references were a huge help during the creation of Jenkinsploit. Thank you!

* Jenkins vulnerabilities and exploits

Credits to Orange Tsai!

    https://blog.orange.tw/2019/01/hacking-jenkins-part-1-play-with-dynamic-routing.html
    https://blog.orange.tw/2019/02/abusing-meta-programming-for-unauthenticated-rce.html

* Scripted attack methods for Jenkins illustrating common vulnerabilities

Credits to gquere!

    https://github.com/gquere/pwn_jenkins

* Jenkinsploit Groovy payloads and scripting console methods

Credits to dennyzhang!

    https://github.com/dennyzhang/cheatsheet-jenkins-groovy-A4

* ASCII Art

Credits to patorjk!

    https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=
