from setuptools import find_packages,setup

from typing import List
def get_requirements(file_path:str) -> List[str]:
    # this function will return a list of string for install_requires
   
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
name = 'mlproject',
version = '0.0.1',
author = 'Shubham',
author_email = 'shubhamsharma2000.007@gmail.com',
packages= find_packages(),

# this takes list of strings as library names.
# better to have a function here.
install_requires= get_requirements('requirements.txt')
)

