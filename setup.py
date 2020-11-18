import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
        long_description = fh.read()

setuptools.setup(
    name="json-api",
    version="0.0.0",
    author="Simon Emmott",
    author_email="simon.l.emmott@yahoo.co.uk",
    description="A utility for defining model classes using json_model from openApi documents",
    long_description=long_description,
    packages=find_packages(exclude=['htmlcov', 'testing', '.vscode', 'docs']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
