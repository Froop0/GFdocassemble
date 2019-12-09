import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AderantFetch", # Replace with your own username
    version="0.0.1",
    author="FFA",
    author_email="Frederik_falsig@yahoo.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Froop0/GFdocassemble",
    packages=['AderantFetch'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)