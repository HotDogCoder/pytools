import sys

from core.util.path.path_helper import PathHelper

parameters = sys.argv
path_helper = PathHelper()


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    if len(lst3) > 0:
        return lst3[0]
    else:
        return False


try:
    flag_val = intersection(('make', 'm'), parameters)
    if flag_val:
        index = parameters.index(flag_val)
        command = parameters[index + 1]

    try:
        if command == "page":
            print(f"-------------------------")
            page_name = parameters[index + 2]
            root_path = path_helper.get_project_root_path()
            path_helper.create_directory(f'{root_path}')


    except IndexError:
        print("ERROR : name parameter is require")

except IndexError:
    print("ERROR : command not found options : ['controller','service','page']")
