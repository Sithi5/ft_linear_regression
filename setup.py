from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["pandas==1.3.3", "matplotlib==3.4.3"]

test_requirements = ["pytest==5.4.3"]

dev_requirements = ["black==21.9b0"] + test_requirements

extra_requirements = {
    "dev": dev_requirements,
}

setup(
    name="ft_linear_regression",
    version="0.0.1",
    description="A linear regression algorithm.",
    long_description=long_description,
    author="Malo Boucé",
    author_email="ma.sithis@gmail.com",
    url="https://github.com/Sithi5/ft_linear_regression",
    py_modules=["ft_linear_regression"],
    packages=["src", "tests"],
    install_requires=requirements,
    extras_require=extra_requirements,
    entry_points={
        "console_scripts": ["linear_regression = src.cli:cli"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
