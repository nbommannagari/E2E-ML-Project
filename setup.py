# Responsible in creating my ML app as a package. I can build my entire ML app as a package and deploy in pypi

from typing import List
from setuptools import find_packages, setup

E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
# =============================================================================
# This function will return the list of requirements (Libraries)
# -e . in requirements.txt file will automatically trigger setup.py file
# =============================================================================
   requirements = []
   with open(file_path) as file_obj:
      requirements = file_obj.readlines()
      # removing new line character from requriements.txt with blank when writing the libs into a list. Also filtering out -e . line into the list of libs using if condition
      requirements = [ req.replace("\n", "") for req in requirements if E_DOT not in req] 
    
   return requirements

setup(
    name='e2emlproject',
    version='1.0.0',
    author='Nanda',
    author_email='ngari.misc@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn','matplotlib']
    install_requires=get_requirements('requirements.txt')
)