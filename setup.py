from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    description="A package for detecting emotions using Watson NLP",
    author="Your Name",
    python_requires=">=3.6",
)
