import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="htp_xtal_mx",
    version="0.0.1",
    author="Gyorgy Babnigg",
    author_email="gbabnigg@gmail.com",
    description="Processing serial crystallography data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gyorgy5635/htp-xtal-mx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)   