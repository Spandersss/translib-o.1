from setuptools import setup, find_packages

setup(
    name="translib0.1",  
    version="0.1.0",                
    author="Spandersss",
    author_email="dpanders10@gmail.com",
    description="A text translation library that overwrites text files using Lingva API, requests, and pathlib",
    long_description='A python library designed to process and translate text files easily via Lingva API.',
    long_description_content_type="text/plain",
    url="https://github.com/Spandersss/translib-o.1", 
    packages=find_packages(),       
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",        
    install_requires=[
        "requests>=2.25.0",         
    ],
)


    
       