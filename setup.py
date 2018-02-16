from setuptools import setup, find_packages


setup(
    name='sanskrit_util',
    version='0.1.1.dev2',
    description='Sanskrit utilities',
    long_description='Collection of utilities for analyzing and working with Sanskrit',

    url='https://github.com/sanskrit/sanskrit',
    author='learnsanskrit.org',
    author_email='info@learnsanskrit.org',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sanskrit',

    packages=find_packages(exclude=['docs', 'test*']),
    install_requires=['sqlalchemy >= 0.7',
                      'future',
                      'six'],
    extras_require={
        'dev': ['pytest'],
        'test': ['pytest'],
    }
)
