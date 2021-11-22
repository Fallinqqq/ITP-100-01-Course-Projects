#from pathlib import Path
#new_dir = Path.home() / "new_directory"
#new_dir.mkdir()

print(new_dir.exists())
new_dir = Path.home()
for path in new_dir.iterdir():
    print()

#new_dir = Path.home() / "downloads"
#for path in new_dir.glob("*zip"):
   #print(path)
