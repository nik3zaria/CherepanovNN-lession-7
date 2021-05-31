import os
filter_by_type = '.'
start_of_line = '|'
start_of_the_name_string = '-'


def creating_a_project():
   with open('config.yaml', 'r', encoding='utf-8') as file:
      folder_and_file_structure = file.read()
      folder_and_file_structure = folder_and_file_structure.splitlines()
      for name in folder_and_file_structure:
         if (name[0] == start_of_line):
            if filter_by_type in name:
               name = name[3:]
               folder_root = os.path.join(name)
               if not os.path.exists(folder_root):
                  open(folder_root, 'w').close()
            else:
               name = name[3:]
               folder_root = os.path.join(name)
               if not os.path.exists(folder_root):
                  os.mkdir(folder_root)
         elif (name[3] == start_of_line and name[5] == start_of_the_name_string):
            if filter_by_type in name:
               name = name[6:]
               first_level_of_nesting = os.path.join(folder_root, name)
               if not os.path.exists(first_level_of_nesting):
                  open(first_level_of_nesting, 'w').close()
            else:
               name = name[6:]
               first_level_of_nesting = os.path.join(folder_root, name)
               if not os.path.exists(first_level_of_nesting):
                  os.mkdir(first_level_of_nesting)
         elif (name[6] == start_of_line and name[8] == start_of_the_name_string):
            if filter_by_type in name:
               name = name[9:]
               second_level_of_nesting = os.path.join(first_level_of_nesting, name)
               if not os.path.exists(second_level_of_nesting):
                  open(second_level_of_nesting, 'w').close()
            else:
               name = name[9:]
               second_level_of_nesting = os.path.join(first_level_of_nesting, name)
               if not os.path.exists(second_level_of_nesting):
                  os.mkdir(second_level_of_nesting)
         elif (name[9] == start_of_line and name[11] == start_of_the_name_string):
            if filter_by_type in name:
               name = name[12:]
               third_level_of_nesting = os.path.join(second_level_of_nesting, name)
               if not os.path.exists(third_level_of_nesting):
                  open(third_level_of_nesting, 'w').close()
            else:
               name = name[12:]
               third_level_of_nesting = os.path.join(second_level_of_nesting, name)
               if not os.path.exists(third_level_of_nesting):
                  os.mkdir(third_level_of_nesting)
         elif (name[12] == start_of_line and name[14] == start_of_the_name_string):
            if filter_by_type in name:
               name = name[15:]
               the_fourth_level_of_nesting = os.path.join(third_level_of_nesting, name)
               if not os.path.exists(the_fourth_level_of_nesting):
                  open(the_fourth_level_of_nesting, 'w').close()
            else:
               name = name[15:]
               the_fourth_level_of_nesting = os.path.join(third_level_of_nesting, name)
               if not os.path.exists(the_fourth_level_of_nesting):
                  os.mkdir(the_fourth_level_of_nesting)


if __name__ == '__main__':
   creating_a_project()
