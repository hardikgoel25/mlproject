from setuptools import setup, find_packages
from typing import List

HYPHEN_E_D ='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_D in requirements:  
            requirements.remove(HYPHEN_E_D)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Hardik',
    author_email='hardik.goel.200525@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)