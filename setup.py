from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


def load_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()


setup(
    name='boil',
    version='0.1.1',
    description='Radically simple app initialization',
    long_description=readme(),
    url='https://github.com/bzurkowski/boil',
    author='Bartosz Zurkowski',
    license='MIT',
    install_requires=load_requirements(),
    packages=find_packages(),
    scripts=['bin/boil'],
    entry_points={
        'boil.plates': [
            'python_package = boil.plates.python_package',
            'python_script = boil.plates.python_script',
            'ansible_role = boil.plates.ansible_role'
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
