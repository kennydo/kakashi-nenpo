from setuptools import setup, find_packages


setup(
    name='kakashi-nenpo',
    version='0.0.1',
    description='Nyaa webooks provider',
    long_description='',
    url='https://github.com/kennydo/kakashi-nenpo',
    author='Kenny Do',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ],
    keywords='nyaa',
    packages=find_packages(),
    install_requires=[
        'Django==1.8.4',
        'nyaalib==0.0.6',
        'requests==2.7.0',
    ],
    tests_require=[
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
