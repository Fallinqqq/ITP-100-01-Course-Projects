# main.py

from mypackage import module1,module2
# import mypackage.module1
# import mypackage.module2

# mypackage.module1.greet("Pythonista")
# mypackage.module2.depart("Pythonista")

from mypackage.module1 import greet as g
from mypackage.module2 import depart as d

g("me")
d("me")
