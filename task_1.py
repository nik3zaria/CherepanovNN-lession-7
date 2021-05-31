import os

subfolder_names = ['settings', 'mainapp', 'adminapp', 'authapp']
for name in subfolder_names:
   dir_path = os.path.join('my_project', name)
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)

