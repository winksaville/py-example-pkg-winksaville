import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='example-pkg-winksaville', # Replace with your own username
    version='0.0.4',
    license='MIT',
    author='Wink Saville',
    author_email='wink@saville.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/winksaville/python-example-pkg-winksaville',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'markdown',
    ],
    python_requires='>=3.8',
)
