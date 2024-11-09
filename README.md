
<h1 align="center">Gif Maker</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/mitchellkolb/gif-maker?color=FD7D00">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/mitchellkolb/gif-maker?color=FD7D00">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mitchellkolb/gif-maker?color=FD7D00">

  <img alt="Github stars" src="https://img.shields.io/github/stars/mitchellkolb/gif-maker?color=FD7D00" />
</p>

<p align="center">
<img
    src="https://img.shields.io/badge/Python-FD7D00?style=for-the-badge&logo=Python&logoColor=white"
    alt="Website Badge" />
<img
    src="https://img.shields.io/badge/Linux-86BE43?style=for-the-badge&logo=linuxmint&logoColor=white"
    alt="Website Badge" />
</p>

This is a Linux designed gif maker app that uses the [gifski](https://gif.ski/) open source encoder library. I'm making this becuase there is an app I use frequently on MacOS that goes by the same name [Gifski](https://github.com/sindresorhus/Gifski) made by [sindresorhus](https://github.com/sindresorhus) that I would love to have remade to run on Linux with a GUI. I'm using this as an opportunity to learn 

---


# Table of Contents
- [What I Learned](#what-i-learned-in-this-project)
- [Tools Used / Development Environment](#tools-used--development-environment)
- [How to Set Up](#how-to-set-up)
- [Project Overview](#project-overview)


---

# What I Learned in this Project
- How to setup the file structure and build files to Flatpak apps
- How to publish an app on Flathub
- Programming with a new UI library PyGObject that uses GTK
- Planning and execution of an app from start to finish



# Tools Used / Development Environment
- Python
- Rust
- PyGObject/GTK
- VS Code
- Terminal
- Linux Mint







# How to Set Up
This project was implemented on my Linux desktop using information from the [PyGOject site](https://pygobject.gnome.org/getting_started.html#ubuntu-getting-started)
- Clone this repository 
- `sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-4.0`
- In the codebase that was cloned create a virtual environment: `python3 -m venv .venv`
- Activate the virtual environment: `source .venv/bin/activate`
- Download External Python Libraries: `pip install -r requirements.txt`
- The program should begin to run: `python3 main.py`






# Project Overview
Simply put this project is intended to be a Linux made GUI version of the Gifski MacOS app.



## Project Details


## Technical Plan
The project employs a 


## Files and Structure
- `main.py`: Contains the code


## Future Work
Future improvements could include






--- 
