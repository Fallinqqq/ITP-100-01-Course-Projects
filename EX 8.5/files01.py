"""How to create paths within files"""

import pathlib
path = pathlib.Path(r"C:\Users\Grace\Desktop\hello.txt")
print(path)
home = pathlib.Path.home()
print(home)
print(pathlib.Path.cwd())
print(pathlib.is_absolute())
###
#home = pathlib.Path.home())
#print(home)
#print(list(path.parents))
###
#home = pathlib.pathhome()
#print(home)
#print(home.name)
#path = home \ "desktop/hello.txt"
#print(path.name)
#print(path.stem)
#print(path.suffix)
###
#print = pathlib.path.home() \ "hello.txt"
#print(path.exsists())
#print(path.home())
