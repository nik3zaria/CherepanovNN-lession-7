import os
import json


def folder_statistics_file():
   folder_statistics = {}
   for item in os.scandir('..\..'):
      if item.is_file():
         size = item.stat().st_size
         threshold = 10 ** len(str(size))
         ext = item.name.split('.')[-1]
         try:
            folder_statistics[threshold][0] += 1
            ext_list = folder_statistics[threshold][1]
            if ext in ext_list:
               pass
            else:
               ext_list.append(ext)

         except (KeyError, IndexError):
            folder_statistics[threshold] = [1, [ext]]

   with open('fileJSON', 'w') as f:
      f.write(json.dumps(folder_statistics))



if __name__ == '__main__':
   folder_statistics_file()
