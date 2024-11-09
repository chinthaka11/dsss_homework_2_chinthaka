from setuptools import setup, find_packages

setup(
    name="dsss_homework_2_chinthaka",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz",
        ],
    },
    author="Chinthaka",
    description="A math quiz game for DSSS homework 2",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chinthaka11/dsss_homework_2_chinthaka",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
