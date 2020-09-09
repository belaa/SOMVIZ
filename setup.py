import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SOMVIZ",
    version="0.0.2",
    author="Bela Abolfathi",
    author_email="babolfat@uci.edu",
    description="Tools for generating and visualizing self-organizing maps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/belaa/SOMVIZ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)