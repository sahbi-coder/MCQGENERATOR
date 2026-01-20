from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Sahbi Kardi",
    author_email="sahbikardipl@gmail.com",
    install_requires=[
      'openai',
      'langchain',
      'streamlit',
      'python-dotenv',
      'PyPDF2',
      'langchain_openai'
    ],
    packages=find_packages()
    
)