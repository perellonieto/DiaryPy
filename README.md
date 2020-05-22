# DiaryPy

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
