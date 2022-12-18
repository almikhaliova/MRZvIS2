import json


def settingData(colum, w1, w2):
    with open('weigh_2.json', 'w', encoding="utf-8") as w:
        temp_dict = {"colum": colum, "w1": w1, "w2": w2}
        json.dump(temp_dict, w, indent=2)


def gettingData():
    with open('weight_2.json', 'r', encoding="utf-8") as note:
        data = json.load(note)
        return data['colum'], data['w1'], data['w2']


def getSequences():
    with open('chain.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data['chain']
