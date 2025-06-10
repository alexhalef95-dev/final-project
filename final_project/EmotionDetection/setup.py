from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Your Name',
    description='A simple package for detecting emotions using Watson NLP API',
    keywords='emotion detection watson nlp',
)
