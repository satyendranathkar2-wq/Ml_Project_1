# Building Entire mechine learning package 
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:#this function will return the list of requirements
    requirements=[]
    with open(file_path) as file_obj:#this will open the file and read the content of the file
        requirements=file_obj.readlines()#this will read all the lines in the file
        requirements=[req.replace('\n',"")for req in requirements]#this will remove the newline character from each line
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name="mlproject",
version="0.0.1",
author="Satyendranathkar",
author_email="satyendranathkar2@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)