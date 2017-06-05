from setuptools import setup, find_packages

setup(
    name="kai",
    version="0.1",
    url="https://github.com/tiffanyjaya/kai.git",
    author="Tiffany Jaya",
    author_email="tiffapedia@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    test_suite="nose.collector",
    tests_require=["nose"],
    install_requires=["pdfminer.six"]
)