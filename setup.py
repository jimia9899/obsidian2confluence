from setuptools import setup, find_packages

setup(
    name='obs2conf',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'atlassian-python-api',
        'markdown2',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'obs2conf=cli:main',
        ],
    },
)
