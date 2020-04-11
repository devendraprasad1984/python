# https://opensource.com/article/18/4/flask


from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_todo',
    version='0.0',
    description='A To-Do List built with Flask',
    author='DP',
    author_email='<Your actual e-mail address here>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)




#
# #!/usr/bin/env python
#
# from distutils.core import setup
#
# setup(name='Distutils',
#       version='1.0',
#       description='Python Distribution Utilities',
#       author='Greg Ward',
#       author_email='gward@python.net',
#       url='https://www.python.org/sigs/distutils-sig/',
#       packages=['distutils', 'distutils.command'],
#       )



