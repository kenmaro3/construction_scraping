#https://craft-bank.com/companies/r4,r5

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import parse
import pickle


def parse_ind(url):
    tmp_list = []
    #data_one_dict["url"].append(url)
    tmp_list.append(url)
    html_ind = urllib.request.urlopen(test3).read()
    soup_ind = BeautifulSoup(html_ind)
    infos = soup_ind.find_all("li", "info-column")
    for info in infos:
        col = info.find("h3")
        if col.text == "社名":
            try:
                tmp = info.find("span").text
                tmp_list.append(tmp)
            except:
                tmp_list.append(None)
            #data_one_dict["name"].append(tmp)
        elif col.text == "売上高":
            try:
                tmp = info.find("span").text
                oku = parse.parse_oku(tmp)
                man = parse.parse_man(tmp)
                tmp_list.append(oku)
                tmp_list.append(man)
            except:
                tmp_list.append(None)
            # data_one_dict["oku"].append(oku)
            # data_one_dict["man"].append(man)
        elif col.text == "現場管理者数":
            try:
                tmp = info.find("span").text
                nin = parse.parse_nin(tmp)
                tmp_list.append(nin)
            except:
                tmp_list.append(None)
            #data_one_dict["manager"].append(nin)
        elif col.text == "自社職人数":
            try:
                tmp = info.find("span").text
                nin = parse.parse_nin(tmp)
                tmp_list.append(nin)
            except:
                tmp_list.append(None)
            #data_one_dict["shokunin"].append(nin)

    return tmp_list
    


if __name__ == "__main__":
    print("hello, world")
    whole_list = []
    pages = 100
    for i in range(pages):
        if i == 0:
            url_base = "https://craft-bank.com/companies"
        else:
            url_base = f"https://craft-bank.com/companies?page={i+1}"

        cols_total = ["url", "name", "oku", "man", "manager", "shokunin"]
        #df = pd.DataFrame()

        page = 0
        # url = url_base.format(page)
        try:
            html = urllib.request.urlopen(url_base).read()
        except:
            raise Exception("url")
        soup = BeautifulSoup(html)
        test = soup.find_all("div", class_="company-card")


        for j in range(len(test)):
            time.sleep(0.5)
            print(f"{j}/{len(test)}==============")
            try:
                test2 = test[j].find("a")
                test3 = test2.get("href")
                tmp_list = parse_ind(test3)
                whole_list.append(tmp_list)
            except:
                pass
        
        df = pd.DataFrame(whole_list, columns=cols_total)
        df.to_csv("tmp.csv")
        print(len(df))
    quit()
    with open("data_df.pkl", "wb") as f:
        pickle.dump(df, f)

    quit()
