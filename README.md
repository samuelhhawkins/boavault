# boavault
Password storage and creation app 

BoaVault is an online password management website

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
	- [Generator](#generator)
- [Badge](#badge)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

BoaVault is a django app using python, html, css and the django framework along with SQLite for development and Postgres for Production DB enviornment. This app was created out of my frustration with how many username email password combos I was trying to keep a hold of. This app contains authorisation using djangos built in function a Home page containg all of users accounts along with a random password generator button still ofline for the time being! we also have a user profile, an about page and a page for making new account posts along with a page for editing and deleting.


## Install

You will need to install django, python3, pip INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'crispy_forms',
    'store.apps.StoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

## Usage

use to store passwords emails and usernames

### Generator

To use the generator, click generate on home page works using simple python random function.

## Maintainers

Samuel Hale Hawkins samuel.h.hawkins@hotmail.com for questions!,,, samuelhhawkins git hub username

## Contributing

Feel free to dive in! [Open an issue](https://github.com/RichardLitt/standard-readme/issues/new) or submit PRs.

Standard Readme follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

## License

Samuel Hawkins for all to use and fuck with!
