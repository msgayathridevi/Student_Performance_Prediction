from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
# this function will return the list of requirements
def get_requirements(file_path:str)->List[str]:
       
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # avoid \n during the fetch
        requirements = [req.replace("\n", "") for req in requirements]

        # to remove the -e .y in the requirements.txt while calling
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='stud_perf_pred',
version='0.0.1',
author='Gayathri Devi',
author_email='msg3dv@gmail.com',
# identifies source as a package itself, checks how many and whr __init_ files are present
packages=find_packages(), # find_package to find and load settings from an external project
# install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)