import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aich",
    version="0.0.1",
    author="Arijit Aich",
    author_email="a2.arijitaich@gmail.com",
    description="Encrypt & Decrypt Words Found In A Local Dictionary. Helpful In Tokenizing Blockchain Wallet Passwords.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arijitaich/AICH-Encryption",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)