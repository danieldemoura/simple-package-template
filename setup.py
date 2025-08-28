from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hello_world_dio_2025",
    version="0.0.1",
    author="Daniel",
    author_email="my_email",
    description="Só um teste de criação de um pacote Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danieldemoura/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)