from setuptools import  find_packages, setup
from typing import List

HYPEN_E_DIT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''This func will return the list of requrements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DIT in requirements:
            requirements.remove(HYPEN_E_DIT)
        
    return requirements
        

setup(
    name='mlproject',
    version='0.0.1',
    author='Hristo',
    author_email='hr.nikolov3@gmail.com',
    packages=find_packages(),
    install_requres=get_requirements('requirements.txt')    
)