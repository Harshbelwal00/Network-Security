from gettext import install
from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirement.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")
    
    return requirement_lst

print(get_requirement())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Harsh Singh",
    author_email="harsh.singh.belwal278@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)