[![CI][ci:b]][ci]
[![Documentation][documentation:b]][documentation]
[![License MIT][license:b]][license]
![Python3.8][python:b]
[![pypi][pypi:b]][pypi]
[![codecov][codecov:b]][codecov]

[ci]: https://github.com/perellonieto/DiaryPy/actions/workflows/ci.yml
[ci:b]: https://github.com/perellonieto/diarypy/workflows/CI/badge.svg
[license]: https://github.com/perellonieto/DiaryPy/blob/master/LICENSE.txt
[license:b]: https://img.shields.io/github/license/perellonieto/diarypy.svg
[python:b]: https://img.shields.io/badge/python-3.8-blue
[pypi]: https://badge.fury.io/py/diarypy
[pypi:b]: https://badge.fury.io/py/diarypy.svg
[codecov]: https://codecov.io/gh/perellonieto/DiaryPy
[codecov:b]: https://codecov.io/gh/perellonieto/DiaryPy/branch/master/graph/badge.svg?token=AYMZPLELT3


# DiaryPy

### A python class to automatically save the partial/intermediary results of a running experiment in a set of notebooks (csv files) and images as files.

[![Build Status](https://travis-ci.org/perellonieto/DiaryPy.svg?branch=master)](https://travis-ci.org/perellonieto/DiaryPy)

Create a new diary

```
diary = Diary(name='world', path='hello', overwrite=False)
```

Create all the notebooks that you want to use

```
diary.add_notebook('validation')
diary.add_notebook('test')
```

Store your results in the different notebooks

```
diary.add_entry('validation', ['accuracy', 0.3])
diary.add_entry('validation', ['accuracy', 0.5])
diary.add_entry('validation', ['accuracy', 0.9])
diary.add_entry('test', ['First test went wrong', 0.345, 'label_1'])
```

Add some image

```
image = Image.new(mode="1", size=(16,16), color=0)
diary.save_image(image, filename='test_results')
```

### Resulting files

The files that are generated after executing the previous lines are

```
hello/
└── world
    ├── description.txt
    ├── images
    │   └── test_results_4.png
    ├── test.csv
    └── validation.csv
```
the content of the files is

description.txt
```
Date: 2015-10-22 17:43:19.764797
Name : world
Path : hello/world
Overwrite : False
Image_format : png
```

validation.csv
```
1,1,|2015-10-22|,|17:43:19.765404|,|accuracy|,0.3
2,2,|2015-10-22|,|17:43:19.765509|,|accuracy|,0.5
3,3,|2015-10-22|,|17:43:19.765576|,|accuracy|,0.9
```

test.csv
```
4,1,|2015-10-22|,|17:43:19.765657|,|First test went wrong|,0.345,|label_1|
```

# Unittest

```
python -m unittest discover diarypy
```
