import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devendra prasad (thoughtworks battleship game and algo)",
    version="0.0.1",
    author="Devendra Prasad",
    author_email="devendraprasad1984@gmail.com",
    description="thoughtworks battleship game and algo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devendraprasad1984/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)