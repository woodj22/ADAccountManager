from setuptools import setup, find_packages

setup(name='ADAccountManager',
      version='0.1',
      python_requires='>=3',
      packages=find_packages(),
      include_package_data=True,
      description="Manage a active directory user's account using an admin account.",
      url='https://github.com/woodj22/ADAccountManager.git',
      author='woodj22',
      author_email='joe.wood@bbc.co.uk',
      license='MIT',
      install_requires=['ldap3', 'Click'],
      zip_safe=False)