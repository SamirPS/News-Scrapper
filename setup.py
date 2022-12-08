from setuptools import setup,find_packages
from setuptools.command.install import install as _install


class DownloadNLTK(_install):
    def run(self):
        self.do_egg_install()
        import nltk
        required_nltk = [
            'brown',  # Required for FastNPExtractor
            'punkt',  # Required for WordTokenizer
            'maxent_treebank_pos_tagger',  # Required for NLTKTagger
            'movie_reviews',  # Required for NaiveBayesAnalyzer
            'wordnet',  # Required for lemmatization and Wordnet
            'stopwords'
        ]
        for i in required_nltk:
            nltk.download(i)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="newsscrapper-SamirPS",  # Replace with your own username
    version="1.0.2",
    author="SamirPS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamirPS/News-Scrapper",
    install_requires=["requests", "bs4", "lxml","newspaper3k"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    cmdclass={'download_nltk': DownloadNLTK},
)


