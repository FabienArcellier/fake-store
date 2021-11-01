from setuptools import setup
from setuptools import find_packages

setup(
    name='fake-store',
    version='0.2',
    packages=find_packages(exclude=["*_tests.*", "*_tests"]),
    license='MIT license',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires = [
        'pyyaml'
    ],
    extras_require={
        'dev': [
            'alfred-cli',
            'build',
            'pylint',
            'coverage',
            'twine'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Console"
    ],
    url="https://github.com/FabienArcellier/fake-store"
)
