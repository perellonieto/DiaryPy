import os
import re
import pandas as pd
from diarypy.diary import Diary
from diarypy import DESCR_FILENAME
from diarypy import DIARY_VERSION_DELIMITER
from diarypy.diary import FIRST_COLUMNS


def open_all_diaries(name, path, mode='r'):
    folder_regexp = re.compile(".*{0}{1}{2}\d+".format(os.path.sep, name,
                                                       DIARY_VERSION_DELIMITER))
    diary_dict = {}
    for root, subdirs, files in os.walk(path, followlinks=True):
        if folder_regexp.match(root) and (DESCR_FILENAME in files):
            try:
                diary_dict[root] = load_diary(root, mode=mode)
            except ValueError as e:
                print('Diary {} can not be loaded (skipped)'.format(root))
                print(e)
    return diary_dict


def merge_notebooks(diary_dict, notebook_name_list):
    notebooks_list_df = []
    for diary in diary_dict.values():
        found = 0
        for i, notebook_name in enumerate(notebook_name_list):
            if notebook_name in diary.notebooks:
                if i == 0:
                    notebooks_same_diary_df = notebook_to_dataframe(diary.notebooks[notebook_name])
                else:
                    notebooks_same_diary_df = notebooks_same_diary_df.merge(
                        notebook_to_dataframe(diary.notebooks[notebook_name]),
                        how='cross', suffixes=['', '_' + notebook_name])
                found += 1
            else:
                break
        if found == len(notebook_name_list):
            notebooks_list_df.append(notebooks_same_diary_df)
    notebooks_df = pd.concat(notebooks_list_df)
    return notebooks_df


def notebook_to_dataframe(notebook):
    if notebook.has_header:
        notebook_df = pd.DataFrame(notebook.history)
    else:
        header = FIRST_COLUMNS + notebook.history[0][len(FIRST_COLUMNS)::2]
        columns_id = [i if i < len(FIRST_COLUMNS) else i + (1 + i - len(FIRST_COLUMNS))
                      for i in range(len(header))]
        rows = [[row[c] for c in columns_id] for row in notebook.history]
        notebook_df = pd.DataFrame(rows, columns=header)
    return notebook_df


def load_diary(path, mode='r'):
    diary = Diary(name=None, path=path, overwrite=True, mode=mode)
    return diary
