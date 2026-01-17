from setuptools import setup, find_packages

setup(
    name='grok-sentiment',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'torch'
    ],
    description='Simple Grok-inspired sentiment analyzer using FinBERT',
    author='RONMCG1',
    license='MIT',
    url='https://github.com/RONMCG1/grok-sentiment'
)
