try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project in Python',
    'author': 'Octavian Muntean',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'unkn0wn27@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['unknown'],
    'scripts': [],
    'name': 'unknown'
}

setup(**config)
