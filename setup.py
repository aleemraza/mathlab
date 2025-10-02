from setuptools import setup, find_packages
setup(
    name="mathlab",  # This will be your package name on PyPI
    version="0.1.0",
    packages=find_packages(),
    description="A lightweight Python math library with arithmetic, algebra, geometry, and number theory utilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Muhammad Aleem Raza",
    author_email="aleemraza661@gmail.com",
    url="https://github.com/aleemraza/mathlab.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)