# -*- coding: utf-8 -*-
"""bj1157.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xGhWspuX7CVWdO4UMhrQtTxrbhLmCvNL
"""

# no.1157
from collections import Counter

str1 = input().upper()

c = Counter(str1)
cnt = c.most_common(2)
cnt3 = [x[0] for x in cnt]

if len(str1) == 1:
    print(str1)
elif cnt[0][1] != cnt[1][1]:
    print(cnt[0][0])
else:
    print("?")

list(dict(c).keys())[0]
# elif len(c) == len(str1):
#     tmp = sorted(cnt3, reverse=True)
#     print(tmp[0])