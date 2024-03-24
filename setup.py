from setuptools import setup

setup(
    name='tree-2-md',
    version='1.0.0',
    py_modules=['tree_2_md'],
    entry_points={
        'console_scripts': [
            'tree-2-md = tree_2_md:main',
        ],
    },
)