from setuptools import setup, find_packages

setup(
    name='epgm_model',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'pandas',
        'matplotlib',
        'scipy'
    ],
    author='Haris Masood',
    author_email='haris_masood@yahoo.com',
    description='Implementation of the EPGM model for time series forecasting.',
    license='MIT Open Source License',  
    classifiers=[
        'Development Status :: 1 - Production',  
        'Intended Audience :: Quantitative Finance/Algorithmic Trading',
        'Programming Language :: Python :: 3',
        'Topic :: Quanitative Finance/Algorithmic Trading',
    ],
)