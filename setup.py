from setuptools import setup, find_packages

setup(
      name='sapai_gym',
      version='0.1.0',
      packages=find_packages(),
      install_requires=[
          "sapai @ git+https://github.com/teknogeek/sapai.git@main",
          "gym~=0.21.0",
          "scikit-learn"
      ]
)
