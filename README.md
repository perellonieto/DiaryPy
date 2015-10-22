# DiaryPy

- Create a new diary

    diary = Diary(name='world', path='hello', overwrite=False)

- Create all the notebooks that you want to use

    diary.add_notebook('validation')
    diary.add_notebook('test')

- Store your results in the different notebooks

    diary.add_entry('validation', ['accuracy', 0.3])
    diary.add_entry('validation', ['accuracy', 0.5])
    diary.add_entry('validation', ['accuracy', 0.9])
    diary.add_entry('test', ['First test went wrong', 0.345, 'label_1'])

- Add some image

    image = Image.new(mode="1", size=(16,16), color=0)
    diary.save_image(image, filename='test_results')
