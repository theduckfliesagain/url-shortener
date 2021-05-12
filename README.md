# URLess

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

Shorten (or slightly lengthen until we get a shorter domain) your URLs in one easy click!

## Installation & Usage

Visit [URLess](https://urlessen.herokuapp.com/)!

Or clone/download the repo and:

* Open a terminal and navigate into the folder
* Run `pipenv install -r requirements.txt` to install dependencies
* Navigate into /shortener/ and run `./manage.py runserver` to start locally

## Technologies
* Python
* Django with templating
* SQLite
* Heroku and PostgreSQL for deployment
* A little bit of Javascript

## Process

* Created base django project and urls app
* Added basic views
* Created URL model, form and view
* Migrated model to database and tested saving/retrieving
* Added generation of short url and display on view as message
* Added styling

## Wins & Challenges

### Wins

* Managed to deploy!

### Challenges

* Deployment

## Bugs

* Let us know!

## Licence

* [MIT licence](https://opensource.org/licenses/mit-license.php) 
