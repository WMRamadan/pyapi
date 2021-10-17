import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyapi-framework",
    version=read("VERSION").strip(),
    author="Wael Ramadan",
    author_email="wamramadan@gmail.com",
    description="A simple python REST api framework.",
    license="GPLv3",
    packages=["src"],
    data_files=["VERSION", "requirements.txt", "README.md", "LICENSE"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/WMRamadan/pyapi-framework",
    install_requires=read("requirements.txt").split("\n"),
    include_package_data=True,
    classifiers=[
              'Intended Audience :: Developers',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Operating System :: MacOS',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Topic :: Software Development',
              'Topic :: Software Development :: Libraries :: Application Frameworks',
          ]
)
