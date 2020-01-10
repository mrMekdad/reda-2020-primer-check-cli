from setuptools import setup

setup(
    name="reda-2020-primer-check-cli",
    version="0.1.0",
    description="CLI focused on primer inventory, length sanity checks, and review reports.",
    author="Red@",
    packages=["primer_check_cli"],
    package_dir={"": "src"},
)
