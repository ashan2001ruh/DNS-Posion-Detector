from setuptools import setup, find_packages
from pathlib import Path

# Read the README file for the long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="dns-poisoning-detector",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "scapy",
        "reportlab",
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "dns_poisoning_detector=src.main:main",  
        ],
    },
    # Metadata for PyPI
    author="Ashan Kasrhuriarachchi",
    author_email="ashandananjana2001@gmailcom",
    description="A DNS poisoning detection tool to detect DNS poisoning attacks.",
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    url="https://github.com/ashan2001ruh/DNS-Posion-Detector",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
    ],
    python_requires=">=3.6",
)