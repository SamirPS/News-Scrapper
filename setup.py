import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newsscrapper-SamirPS", # Replace with your own username
    version="0.1.1",
    author="SamirPS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamirPS/News-Scrapper",
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
