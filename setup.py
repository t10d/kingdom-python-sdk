import setuptools
import toml

config = toml.load("pyproject.toml")["tool"]["poetry"]
config["author"] = ", ".join(
    [" ".join(name_email.split()[:-1]) for name_email in config["authors"]]
)
config["author_email"] = ", ".join(
    [name_email.split()[-1][1:-1] for name_email in config["authors"]]
)

setuptools.setup(
    name=config["name"],
    version=config["version"],
    license=config["license"],
    author=config["author"],
    author_email=config["author_email"],
    description=config["description"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt").read().splitlines(),
    platforms="any",
    packages=setuptools.find_packages(".", exclude=["tests", "tests.*"]),
    python_requires=">=3.9",
    keywords="",
    url="https://github.com/t10d/kingdom-python-core",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
