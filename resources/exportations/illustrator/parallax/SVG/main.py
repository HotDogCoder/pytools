import os

path = '.'  # change this to the path containing your files

for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        new_filename = ""
        name_split = filename.split(' ')
        if len(name_split) > 1:
            new_filename = name_split[1]
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        if new_filename != "":
            print(new_filename)
        else:
            print(filename)
        # os.rename(os.path.join(path, filename), os.path.join(path, new_filename))