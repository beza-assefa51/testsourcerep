from setuptools import setup

setup(
    name='your_project',  # Name of your project/package
    version='0.1',        # Version of your package
    packages=['your_package'],  # List of all packages to include
    entry_points={
        'console_scripts': [
            'render=your_package.main:main',  # Command-line script setup
        ],
    },
)
