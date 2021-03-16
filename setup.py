from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot:main",
        ],
    },
    install_requires=[
        "psutil"
    ],
    version="1.0",
    description="System snapshots maker",
    license="MIT",
    author='Aliaksandr Belski',
    author_email="aliaksandr_belski@epam.com",
)
