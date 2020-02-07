from distutils.core import setup
from distutils.util import convert_path

with open("README.md", 'r') as f:
    long_description = f.read()

main_ns = {}
ver_path = convert_path('diarypy/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
  name = 'diarypy',
  packages = ['diarypy'],
  install_requires=[
    'datetime',
    'Image',
  ],
  version=main_ns['__version__'],
  description = 'Diary to create notebooks and store intermediate results and figures',
  author = 'Miquel Perello Nieto',
  author_email = 'perello.nieto@gmail.com',
  url = 'https://github.com/perellonieto/DiaryPy',
  download_url = 'https://github.com/perellonieto/DiaryPy/archive/{}.tar.gz'.format(main_ns['__version__']),
  keywords = ['diary', 'notebook', 'logging', 'figures', 'experiments'],
  classifiers = [],
  long_description=long_description
)
