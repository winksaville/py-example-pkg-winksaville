import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='example-pkg-winksaville', # Replace with your own username
    entry_points = {
        'console_scripts': ['hello=example_pkg.command_line:main'],
    },
    version='0.0.8',
    license='MIT',
    author='Wink Saville',
    author_email='wink@saville.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/winksaville/py-example-pkg-winksaville',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'markdown',
    ],
    tests_require=[
        'pytest',
    ],
    python_requires='>=3.8',
)
