from setuptools import setup, find_packages

setup(
    name='holiday_jp',
    version='22.10.31',
    url='https://github.com/LUXEYS/holiday_jp-python',
    license='MIT',
    author='Luxeys',
    author_email='tessier@luxeys.com',
    description='Japanese holiday for Python',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
