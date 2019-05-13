from setuptools import setup, find_packages

setup(name='holiday_jp',
      version='19.05.13',
      url='https://github.com/LUXEYS/holiday_jp-python',
      license='MIT',
      author='Luxeys',
      author_email='tessier@luxeys.com',
      description='Japanese holiday for Python',
      long_description_content_type="text/markdown",
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False)
