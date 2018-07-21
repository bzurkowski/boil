from setuptools import setup, find_packages


def get_description():
    with open('README.rst') as readme:
        return readme.read()


def get_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()


setup(
    name='boil',
    version='0.1.4',
    description='Radically simple app initialization',
    long_description=get_description(),
    url='https://github.com/bzurkowski/boil',
    author='Bartosz Zurkowski',
    license='MIT',
    install_requires=get_requirements(),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'boil = boil.cli:main',
        ],
        'boil.plates': [
            'python_package = boil.plates.python_package',
            'python_script = boil.plates.python_script',
            'ansible_role = boil.plates.ansible_role',
            'bash_script = boil.plates.bash_script',
            'license = boil.plates.license',
            'ruby_gem = boil.plates.ruby_gem'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    include_package_data=True,
    zip_safe=False)
