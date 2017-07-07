from setuptools import setup

setup(name='UnlockAccount',
      version='0.1',
      description='unlock a user account using LDAP',
      url='',
      author='woodj22',
      author_email='joe.wood@bbc.co.uk',
      license='MIT',
      packages=['UnlockAccount'],
      entry_points = {
        'console_scripts': ['run=UnlockAccount.command_line:main'],
      },
      install_requires = [
            'python-ldap',
      ],
      zip_safe=False)