import setuptools


setuptools.setup(
    name="clean_folders", 
    version="0.0.1",
    author="VVP",
    author_email="vovvva33@gmail.com",
    description="goit hw 8",
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folders.clean:main'
        ]
    },
    url="https://github.com/vvpwork/goit-python/tree/main/lesson_7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
