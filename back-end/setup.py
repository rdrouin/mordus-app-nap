from setuptools import setup

setup(name='AppNapServer',
      version='1.0',
      description='Server for mordus du transport',
      author='Raphael Drouin',
      author_email='',
      url='',
     install_requires=[ 'flask==0.12.2',
                        'flask-login==0.4.1',
                        'flask_cors==3.0.3',
                        'sqlalchemy==1.2.6',
                        'flask-sqlalchemy==2.3.2',
                        'psycopg2==2.7.4'],
     )
