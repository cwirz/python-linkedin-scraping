"""
My Tool does one thing, and one thing well.
"""
from setuptools import find_packages, setup

dependencies = ['click', 'dpath', 'scrapy', 'tablib']

setup(
    name='linkedin-scraping',
    version='0.1.1',
    url='http://gogs.pyango.ch/cwirz/python-linkedin-scraping.git',
    license='BSD',
    author='Colin Wirz',
    author_email='colin.wirz@me.com',
    description='LinkedIn people search scraper.',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    readme="README.md",
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'linkscrap = linkedin_scraping.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
