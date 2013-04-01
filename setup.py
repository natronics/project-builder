from distutils.core import setup

setup(
    name='project-builder',
    version='0.1',
    description='A set of scripts for automating the creation of a boilerplate web application.',
    author='Nathan Bergey',
    author_email='nathan.bergey@gmail.com',
    url='https://github.com/natronics/project-builder',
    scripts = [
        'scripts/makeproject'
    ]
)
