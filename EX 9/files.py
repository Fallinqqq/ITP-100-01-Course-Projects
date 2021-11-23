# Grace Foster
# ITP 100-01
# EXERCISE: 08
# files.py
# ----------------------------------------------------------------
from pathlib import Path
path = Path.home() / "numbers-1.txt"

linz = "---" * 20
print("This Program will demonstrate various file processing.")
print(linz)

linz = "---" * 20
with path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(text, end="")
file.close()
print(linz)

linz = "---" * 20
with path.open(mode="a", encoding="utf-8") as file:
    file.write("37\n99")
file.close()

with path.open(mode="r", encoding="utf-8") as file:
    text = file.read()
    print(text)
file.close()
print(linz)

lines_of_text = [
    "Grace Foster\n",
    "Freshman\n",
    "Information Systems Technologies\n",
]
with path.open(mode="w", encoding="utf-8") as file:
    file.writelines(lines_of_text)
with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
file.close()

linz = "---" * 20
print(linz)
print("The Program has ended normally!")
