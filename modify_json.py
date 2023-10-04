import json
# 讀入原始檔案
with open('context.json', 'r', encoding="utf-8") as f:
    full_context = json.load(f)
with open('train.json', 'r', encoding="utf-8") as f:
    train = json.load(f)
with open('valid.json', 'r', encoding="utf-8") as f:
    valid = json.load(f)

# train調整
modify_train_list = []
for item in train:
    modify_single_dic = {}
    
    modify_single_dic['id'] = item['id']
    
    lable = 0
    for idx, paragraph_num in enumerate(item['paragraphs']): 
        modify_single_dic[f'ending{idx}'] = full_context[paragraph_num]
        if item['relevant'] == paragraph_num:
            lable = idx
    
    modify_single_dic['label'] = lable
    modify_single_dic['sent1'] = item['question']
    modify_single_dic['sent2'] = item['question']
    
    modify_train_list.append(modify_single_dic)

# valid調整
modify_valid_list = []
for item in valid:
    modify_single_dic = {}
    
    modify_single_dic['id'] = item['id']
    
    lable = 0
    for idx, paragraph_num in enumerate(item['paragraphs']): 
        modify_single_dic[f'ending{idx}'] = full_context[paragraph_num]
        if item['relevant'] == paragraph_num:
            lable = idx
    
    modify_single_dic['label'] = lable
    modify_single_dic['sent1'] = item['question']
    modify_single_dic['sent2'] = item['question']
    
    modify_valid_list.append(modify_single_dic)

# train轉成json
json_data = json.dumps(modify_train_list, ensure_ascii=False)
with open("modify_train.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)
    
# valid轉成json
json_data = json.dumps(modify_valid_list, ensure_ascii=False)
with open("modify_valid.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

# 讀入看看
with open('modify_train.json', 'r', encoding="utf-8") as f:
    modify_train_test = json.load(f)
print(modify_train_test[42])