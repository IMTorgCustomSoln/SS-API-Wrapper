from setuptools import setup, find_packages


setup(
    name='ScrumSaga-API-Wrapper',
    author='Jason Beach',
    author_email='information@mgmt-tech.org',
    description='Wrapper code for ScrumSaga.com API',
    license='MIT',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['argparse'],
    entry_points={
        'console_scripts': [
            'aSimple=aSimple.__main__:main'
        ]
    }
)
