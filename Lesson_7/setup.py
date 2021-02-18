import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clean_folders", # Replace with your own username
    version="0.0.1",
    author="VVP",
    author_email="vovvva33@gmail.com",
    description="goit hw 8",
    url="https://github.com/vvpwork/goit-python/tree/main/lesson_7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)