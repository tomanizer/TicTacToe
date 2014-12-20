try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TicTacToe',
    'author': 'Thomas Haederle',
    'url': 'www.tictactoe.com',
    'download_url': 'Where to download it.',
    'author_email': 'thomas.haederle@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['TicTacToe'],
    'scripts': [],
    'name': 'TicTacToe'
}

setup(**config)