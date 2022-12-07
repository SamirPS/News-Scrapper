import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newsscrapper-SamirPS",  # Replace with your own username
    version="1.0.0",
    author="SamirPS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamirPS/News-Scrapper",
    install_requires=["requests", "bs4", "lxml"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
