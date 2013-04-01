# project-builder

A set of scripts for automating the creation of a boilerplate web application.


## Install

Edit the `CONFIG` settings at the top of `scripts/makeproject` with your
preferences and then install with

    $ sudo python setup.py install


## Use

When you want to create a new project just type `makeproject` and a creative name
for your idea.

    $ makeproject Lemon Squirrels


This will (TODO)
 - create a folder
 - add a boilerplate HTML5 site run with python flask
 - copy in up to date bootstrap and jquery
 - add nice webfonts
 - make a blank favicon svg file for later editing
 - create a virtual environment
 - pip install flask and gunicorn
 - set up a Procfile for pushing to heroku
 - init git repository with readme and .gitignore
 - create a gh-pages branch for documentation
