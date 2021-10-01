 
from setuptools import setup, find_packages

with open('LICENSE') as license_file:
    license_str= license_file.read()
    
setup(name='liboptions',
      version='0.9.0',
      description='Module used to handle string-based options.',
      author='Claudio Romero',
      license=license_str,
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      python_requires=">=3.6")
