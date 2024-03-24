from setuptools import setup

setup(
    name='tree2md',
    version='1.0.0',
    py_modules=['tree2md'],
    entry_points={
        'console_scripts': [
            'tree2md = tree2md:main',
        ],
    },
)