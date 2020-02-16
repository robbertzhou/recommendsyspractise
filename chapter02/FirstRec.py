# -*- coding:utf-8 -*-

import os
import json
import random
import math

class FirstRec:
    """
      初始化函数：
         filePath:原始文件路径
         seed:产生随机数的种子
         k:选取的近邻用户个数
         n_items:为每个用户推荐的电影数
    """
    def __init__(self,file_path,seed,k,n_items):
        self.file_path = file_path
        self.seed = seed
        self.n_items = n_items
        self.k = k
        self.users_1000 = self.__select_1000_users()
        self.train,self.test = self.__load_and_split_data()
        pass

    def __select_1000_users(self):
        print("随机选取1000个用户")
        if os.path.exists("../data/train.json") and os.path.exists("../data/test.json"):
            return list()
        else:
            users = set()
            for file in os.listdir(self.file_path):
                one_path = "{}/{}".format(self.file_path,file)
                with open(one_path,"r") as fp:
                    for line in fp.readlines():
                        if line.strip().endswith(":"):
                            continue
                        userID,_,_ = line.split(",")
                        users.add(userID)
            users_1000 = random.sample(list(users),1)
            return users_1000

    def __load_and_split_data(self):
        train = dict()
        test = dict()
        random.seed(seed)
        for file in os.listdir(self.file_path):
            one_path = "{}/{}".format(self.file_path,file)
            print("{}".format(one_path))
            with open(one_path,"r") as fp:
                movieID = fp.readline().split(":")[0]
                for line in fp.readlines():
                    if line.endswith(":"):
                        continue
                    userID,rate,_ = line.split(",")
                    if(userID in self.users_1000):
                        if random.randint(1,50) == 1:
                            test.setdefault(userID,{})[movieID] =int(rate)
                        else:
                            train.setdefault(userID,{})[movieID] = int(rate)
            json.dump(train,open("data/train.json","w"))
            json.dump(test,open("data/test.json","w"))


if __name__ == "__main__":
    file_path = "../data/netflix/training_set"
    seed = 30
    k = 15
    n_items = 20
    f_rec = FirstRec(file_path,seed,k,n_items)