# importing re (regular expressions) / they use metacharacters to denote different patterns.
import re
fynd = re.findall("ab*c", "c")
print(fynd)
fynd = re.findall("ab*c", "abcd")
print(fynd)
fynd = re.findall("ab*c", "abcac")
print(fynd)
# ------
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
print(string)

