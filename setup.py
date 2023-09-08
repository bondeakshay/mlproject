from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will retuern the string requirnments
    '''
    requirnments = []
    with open(file_path) as file1:
        requirnments = file1.readlines()
        requirnments = [req.replace("\n","") for req in requirnments]
        if HYPEN_E_DOT in requirnments:
            requirnments.remove(HYPEN_E_DOT)

    return requirnments


setup(
    name='mlproject',
    version='0.0.1',
    author='akshay bonde',
    author_email='bondeakshay03@gmail.com',
    packages=find_packages(),
    install_requires =get_requirements('requirnments.txt')
)