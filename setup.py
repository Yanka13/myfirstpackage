from setuptools import setup

from setuptools import find_packages

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]
print(requirements)
setup(name="toto", description="first package",
      packages=find_packages(), scripts=["scripts/who_am_i"],
      install_requires=requirements)
