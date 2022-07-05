import re

def parse_oku(x):
    res = re.findall(r'\d*億', x)
    if res is not None:
        if len(res) > 0:
            return res[0].split("億")[0]
        else:
            res.split("億")[0]
    else:
        return None

def parse_man(x):
    res = re.findall(r'\d*万円', x)
    if res is not None:
        if len(res) > 0:
            return res[0].split("万円")[0]
        else:
            res.split("万円")[0]
    else:
        return None

def parse_nin(x):
    res = re.findall(r'\d*人', x)
    if res is not None:
        if len(res) > 0:
            return res[0].split("人")[0]
        else:
            res.split("人")[0]
    else:
        return None

if __name__ == "__main__":
    print('hello, world')
    test = " 2019年: 5億6000万円"
    test = "9人"
    nin = parse_nin(test)
    print(f"nin: {nin}")

    # oku = parse_oku(test)
    # man = parse_man(test)

    # print(f"oku: {oku}")
    # print(f"man: {man}")