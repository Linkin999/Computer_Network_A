import mimetypes
import os
from typing import Any, Dict

from keyring.testing.util import random_string

# path = 'D:\Study in SUSTech\First semester of junior year\Computer Network A\lab3\practice2'
# for file_name in os.listdir(path):
#     print(mimetypes.guess_type(file_name)[0])
#
#
# CountryCodeDict = {"India": 91, "UK" : 44 , "USA" : 1, "Spain" : 34}
# a="hhhhhhh"
# print(CountryCodeDict)
#
# CountryCodeDict.update({'Germany': 'SESSION_KEY='+a})
#
# print(CountryCodeDict)
# print(CountryCodeDict["Germany"])
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# session_key = "hhhhhhhhh"
# session1: Dict[str, Any] = dict()
# session1 = {"SESSION_KEY=":f"{session_key}"}
# print(session1)
# session2: Dict[str, Any] = dict()
# session2.update({'SESSION_KEY': 'SESSION_KEY=' + session_key})
# print(session2)
session_key = "hhhhhhhhh"
session1="SESSION_KEY="+ session_key
session2: Dict[str, Any] = dict()
session2.update({'SESSION_KEY': 'SESSION_KEY=' + session_key})
if session1 == session2["SESSION_KEY"]:
    print("correct")
