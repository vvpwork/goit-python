from setuptools import setup, find_packages
setup(
    name="clean_folder",
    version="0.0.1",
    author="VVP",
    author_email="vovvva33@gmail.com",
    description="goit hw 8",
    install_requires=[
        'six==1.15.0',
        'transliterate == 1.10.2'
    ],
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.clean:main'
        ]
    },
    # url="https://github.com/vvpwork/goit-python/tree/main/lesson_7",
    packages=find_packages(include=['clean_folder', 'clean_folder.clean']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
