#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

__version__ = "0.0.2"

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.1.2", "requests==2.26.0"]

test_requirements = [
    "pytest>=3",
]

exec(open("coredotfile/version.py").read())
setup(
    author="CoreDotToday",
    author_email="engine@core.today",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Easy to download files without burning your memory",
    entry_points={
        "console_scripts": [
            "series=series.cli:main",
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="coredotfile",
    name="coredotfile",
    packages=find_packages(),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/coredottoday/CoreDotFile.git",
    version=__version__,
    zip_safe=False,
)
