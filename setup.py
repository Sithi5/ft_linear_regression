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
    description="A calculator interpreter.",
    long_description=long_description,
    author="Malo Boucé",
    author_email="ma.sithis@gmail.com",
    url="https://github.com/Sithi5/computorv2",
    py_modules=["computorv2"],
    packages=["src", "gui", "tests"],
    install_requires=requirements,
    extras_require=extra_requirements,
    entry_points={
        "console_scripts": ["computorv2 = computorv2:main"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
