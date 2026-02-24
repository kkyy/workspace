
# coding:utf-8
# 房间里有100个人，每人都有100元钱，他们在玩一个游戏。
# 每轮游戏中，每个人都要拿出一元钱随机给另一个人，最后这100个人的财富分布是怎样的？
import matplotlib.pyplot as plt
import pandas as pd
import random
person = 100
ini_wealth = 100
id_list = range(person)
id_money_dict = {k: ini_wealth for k in id_list}
id_list = list(id_list)
round_number = 17000
for round in range(round_number):
    for id in id_money_dict.keys():
        id_money_dict[id] += -1

        id_list.remove(id)
        id_get = random.choice(id_list)
        id_list.append(id)
        id_list.sort()

        id_money_dict[id_get] += 1
se = pd.Series(id_money_dict)
se.plot.bar()
plt.show()
se.plot.hist(bins=100)