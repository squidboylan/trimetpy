from setuptools import setup, find_packages

setup(
    name='trimetpy',
    version = '0.1.dev1',
    description = 'A python module that wraps trimet\'s api',
    url='https://github.com/squidboylan/trimetpy',
    author='Caleb Boylan',
    author_email='calebboylan@gmail.com',
    license = 'Apache Software License',
    platforms='any',
    packages=find_packages(),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish
        # (should match "license" above)
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
        ],
    keywords='trimet api',
    install_requires=['requests', 'xmltodict'],
    )
