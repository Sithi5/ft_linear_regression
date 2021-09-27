from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

requirements = []

test_requirements = ["pytest==5.4.3", "black==21.7b0"]

extra_requirements = {
    "dev": test_requirements,
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
        "console_scripts": ["linear_regression = linear_regression:main"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
