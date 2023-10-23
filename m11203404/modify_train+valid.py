import json

# 讀入原始檔案
with open('context.json', 'r', encoding="utf-8") as f:
    full_context = json.load(f)
with open('train.json', 'r', encoding="utf-8") as f:
    train = json.load(f)
with open('valid.json', 'r', encoding="utf-8") as f:
    valid = json.load(f)
'''
Paragraph
'''
# modify Paragraph train and valid
modify_Paragraph_list = []
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
    
    modify_Paragraph_list.append(modify_single_dic)

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
    
    modify_Paragraph_list.append(modify_single_dic)

json_data = json.dumps(modify_Paragraph_list, ensure_ascii=False)
with open("modify_total_Paragraph.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

'''
QA
'''
modify_QA_list = []
for item in train:
    modify_single_dic = {}
    
    modify_single_dic['id'] = item['id']
    modify_single_dic['answers'] = {'answer_start': [item['answer']['start']], 'text': [item['answer']['text']]}
    modify_single_dic['context'] = full_context[item['relevant']]
    modify_single_dic['question'] = item['question']
    
    modify_QA_list.append(modify_single_dic)

for item in valid:
    modify_single_dic = {}
    
    modify_single_dic['id'] = item['id']
    modify_single_dic['answers'] = {'answer_start': [item['answer']['start']], 'text': [item['answer']['text']]}
    modify_single_dic['context'] = full_context[item['relevant']]
    modify_single_dic['question'] = item['question']
    
    modify_QA_list.append(modify_single_dic)

json_data = json.dumps(modify_QA_list, ensure_ascii=False)
with open("modify_total_QA.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)