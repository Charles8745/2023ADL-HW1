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
    modify_single_dic['answers'] = {'answer_start': [item['answer']['start']], 'text': [item['answer']['text']]}
    modify_single_dic['context'] = full_context[item['relevant']]
    modify_single_dic['question'] = item['question']
    
    modify_train_list.append(modify_single_dic)

# valid調整
modify_valid_list = []
for item in valid:
    modify_single_dic = {}
    
    modify_single_dic['id'] = item['id']
    modify_single_dic['answers'] = {'answer_start': [item['answer']['start']], 'text': [item['answer']['text']]}
    modify_single_dic['context'] = full_context[item['relevant']]
    modify_single_dic['question'] = item['question']
    
    modify_valid_list.append(modify_single_dic)

# train轉成json
json_data = json.dumps(modify_train_list, ensure_ascii=False)
with open("modify_train_QA.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)
    
# valid轉成json
json_data = json.dumps(modify_valid_list, ensure_ascii=False)
with open("modify_valid_QA.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

# 讀入看看
with open('modify_train_QA.json', 'r', encoding="utf-8") as f:
    modify_train_test = json.load(f)
    
print(modify_train_test[42])

