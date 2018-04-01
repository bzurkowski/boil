from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='boil',
    version='0.1',
    description='Radically simple and versatile app initialization',
    long_description=readme(),
    url='https://github.com/bzurkowski/boil',
    author='Bartosz Zurkowski',
    license='MIT',
    packages=['boil'],
    scripts=['bin/boil'],
    entry_points={
        'boil.plates': [
            'python_package = boil.plates.python_package',
            'python_script = boil.plates.python_script'
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
    zip_safe=False)
