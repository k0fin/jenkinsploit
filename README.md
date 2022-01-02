# Jenkinsploit Framework

## Overview

Jenkinsploit is an attack and exploitation framework tailored toward Jenkins. It was written to provide a single solution for offensive security professionals to quickly map, enumerate, and attack misconfigured Jenkins instances.

## Features

The Jenkinsploit Framework includes a broad list of features, including:

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

## Installation & Usage

    git clone https://github.com/k0fin/jenkinsploit-framework.git
    cd jenkinsploit-framework
    python3 -m pip install -r requirements.txt
    sudo python3 ./setup.py install

    jenkinsploit --help

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

The following references were a huge help during the creation of the Jenkinsploit Framework. Thank you!

* Orange Tsai

    https://blog.orange.tw/2019/01/hacking-jenkins-part-1-play-with-dynamic-routing.html
    https://blog.orange.tw/2019/02/abusing-meta-programming-for-unauthenticated-rce.html

* gquere

    https://github.com/gquere/pwn_jenkins
