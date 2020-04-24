import os
from setuptools import setup, find_packages

readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "README.md"))
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="paratech_mvp_one",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    # metadata to display on PyPI
    url="https://bonicim@bitbucket.org/bonicim/mvp_one.git",
    author="Mark Bonicillo",
    author_email="markabonicillo@gmail.com",
    long_description=readme,
    license="MIT",
)
