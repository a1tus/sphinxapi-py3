from setuptools import setup, find_packages

setup(
    name='sphinxapi-py3',
    version='2.1.9-release',
    description='Python 3 port of official python client for Sphinx Search',
    long_description=open('README.md').read(),
    author='Sphinx Technologies Inc.',
    url='https://github.com/a1tus/sphinxapi-py3',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)