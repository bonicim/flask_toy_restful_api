import os
from setuptools import setup, find_packages

readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "README.md"))
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="my_app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
    # metadata to display on PyPI
    long_description=readme,
)
