import os
from shutil import copyfile


def copying_directories(directory_root):
   for root, dirs, files in os.walk(directory_root):
      for file in files:
         if file.endswith('.html'):
            directory_name = os.path.join('templates', os.path.basename(root))
            if not os.path.exists(directory_name):
               os.makedirs(directory_name)

            copyfile(os.path.join(root, file), os.path.join(directory_name,file))


if __name__ == '__main__':
   copying_directories('my_project')
