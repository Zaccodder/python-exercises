"""Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

from datetime import datetime
exam_st_date = (11, 12, 2014)
res =list(exam_st_date)

print(f"{res[0]}/{res[1]}/{res[2]}")