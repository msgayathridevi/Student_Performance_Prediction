from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        # to remove the -e .y in the requirements.txt while calling
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='generic_ml_project',
version='0.0.1',
author='Gayathri Devi',
author_email='gayudevi.2002@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)