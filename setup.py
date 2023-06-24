from setuptools import setup, find_packages

setup(
    name='instagram-to-discord',
    version='0.1',
    license='GNU GPLv3',
    author="Jonathan Dyallo",
    author_email='contacto@jonathan.com.ar',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/jd-apprentice/instagram-to-discord',
    keywords='integration, instagram, discord, python, webhooks',
    install_requires=[
          'requests',
          'certifi',
          'idna',
          'instaloader',
          'urllib3'
      ],

)