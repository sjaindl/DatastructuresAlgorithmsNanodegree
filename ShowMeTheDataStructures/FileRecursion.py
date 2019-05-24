import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if path == None or suffix == None:
        return None

    suffix_file_list = []

    dir_list = os.listdir(path)
    for item in dir_list:
        if os.path.isfile(os.path.join(path, item)) and item.endswith(suffix):
            suffix_file_list.append(os.path.join(path, item))
        elif os.path.isdir(os.path.join(path, item)):
            suffix_file_list += find_files(suffix, os.path.join(path, item))

    return suffix_file_list

print('*** Test File Recursion ***')
print(find_files('.c', './testdir'))
assert find_files('.c', './testdir') == ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c'], "Not all or wrong files found"
print(find_files('.h', './testdir'))
assert find_files('.h', './testdir') == ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h'], "Not all or wrong files found"
print(find_files('.py', './testdir'))
assert find_files('.py', './testdir') == [], 'No python files here, this should be an empty array!'
print(find_files('', './testdir'))
assert find_files('', './testdir') == ['./testdir/.DS_Store', './testdir/subdir4/.gitkeep', './testdir/subdir3/.DS_Store', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir2/.gitkeep', './testdir/subdir5/a.h', './testdir/subdir5/a.c', './testdir/t1.h', './testdir/subdir1/a.h', './testdir/subdir1/a.c'], 'Search without suffix should return all files!'
print(find_files(None, './testdir'))
assert find_files(None, './testdir') == None, 'Invalid path should return None'
print(find_files('', None))
assert find_files('', None) == None, 'Invalid suffix should return None'
print(find_files('.c', './testdir/subdir3'))
assert find_files('.c', './testdir/subdir3') == ['./testdir/subdir3/subsubdir1/b.c'], "Not all or wrong files found in subdirectory"
print('*** Success ***')
