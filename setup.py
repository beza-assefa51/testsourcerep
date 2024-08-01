from setuptools import setup, find_packages

setup(
    name='testsourcerep',  # Replace with your project name
    version='0.1',
    packages=find_packages(),  # Automatically find packages in the project
    entry_points={
        'console_scripts': [
            'render=my_render_package.main:main',  # Maps the command 'render' to the main function
        ],
    },
)
