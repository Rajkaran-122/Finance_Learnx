from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

# Read requirements.txt, ignore comments
try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except FileNotFoundError:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name="FLX",
    version="1.0.0",
    include_package_data=True,
    author="Digital Metro",
    author_email="",
    url="",
    license="MIT",
    packages=find_packages(),
    description="FLX: Financial Reinforcement Learning Framework for Automated Quantitative Trading.",
    long_description="A deep reinforcement learning framework for automated quantitative trading — covering data acquisition, model training, backtesting, and live paper trading.",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="Reinforcement Learning, Finance, Quantitative Trading",
    platform=["any"],
    python_requires=">=3.7",
)
