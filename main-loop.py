# Looping with For
# myList = ["list one", "list two", "list there"]
# for list in myList :
#  print (list)

""" 
*****
*****
*****
*****
***** 
"""
# string = ''
# for i in range(5):
#     # print({"i" : i})
#     for j in range(5):
#         string += '*'
#     print(string)
#     string = ''
    
""" 
*
**
***
****
***** 
"""

string = ''
for i in range(1,5+1) :
  for j  in range(i):
    string += "*"
  print(string)
  string = ''