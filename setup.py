from setuptools import setup , find_packages
from typing import List

# Design of setup file
"""
    setup requiremet
    read our requirements file 
    remove \n from requirements filem
"""

PROJECT_NAME = "Customer Personality Analysis Project"
VERSION = "0.0.1"
DESCRIPTION = "Modular coding for the customer personality analysis project"
AUTHOR = "Sumeet"
HYPHEN_E_DOT ="-e ."
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirement_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_list:
        requirement_list = requirement_list.readlines()
        requirement_list = [requirement_list.replace("\n", "") for requirement_list in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    

setup(
    name= PROJECT_NAME,
    version= VERSION,
    description= DESCRIPTION,
    author_email= "maheshwarisumeet128@gmail.com",
    author= AUTHOR,
    packages= find_packages(),
    install_requires = get_requirement_list()
)


