# Gtk-Pass: A simple GTK pass viewer

## Pre-requisites
* Linux distribution (tested on Gentoo)
* pass: 1.7.3+ https://www.passwordstore.org/
* python: 3.9+
* pygobject: 3.42.0+
* pinentry with Gtk enabled: 1.2.0+
* `pass` store needs to be set up. Either in environment variable `PASSWORD_STORE_DIR` or in user's directory as a `.password-store`. Read more at https://www.passwordstore.org/
* `pass` should be available to execute in `PATH`

## How to run
* make sure that you've met pre-requisites
* execute `python gtkpass.py`
* alternatively: ```./gtkpass.py```
* enjoy

## Issues:
* The app has a very minimal error processing as the current version is best suited for my personal use
* The app does not provide any ability to modify your passwords/secrets. Use `pass` in a meantime
* The app is tested on Gentoo. It have not been tested on any other distribution
* The app shows everything as one long list, whereas `pass` gives ability to organize passwords/secrets.

## TODO:
* Explore how to display 'organized' view.
* Add an ability to add/remove a password/secret.
* Add error handling as encounter issues.

## TLDR
It's a personal project that was written in a couple of days.
