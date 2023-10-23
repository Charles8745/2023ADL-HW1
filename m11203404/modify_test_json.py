import json
import sys

# load path
context_path = sys.argv[1]
print("context_path:", context_path, '\n')
test_path = sys.argv[2]
print("test_path:", test_path, '\n')
prediction_path = sys.argv[3]
print("prediction_path:", prediction_path, '\n')

# 讀入原始檔案
with open(context_path, 'r', encoding="utf-8") as f:
    full_context = json.load(f)
with open(test_path, 'r', encoding="utf-8") as f:
    test = json.load(f)

modify_test_list = []
for item in test:
    modify_single_dic = {}
    
    modify_single_dic['id'] = item['id']
    
    lable = 0
    for idx, paragraph_num in enumerate(item['paragraphs']): 
        modify_single_dic[f'ending{idx}'] = full_context[paragraph_num]
    
    modify_single_dic['sent1'] = item['question']
    modify_test_list.append(modify_single_dic)

# test轉成json
json_data = json.dumps(modify_test_list, ensure_ascii=False)
with open("./2023ADLHW1/json/modify_test_Paragraph.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

# 讀入看看
with open('./2023ADLHW1/json/modify_test_Paragraph.json', 'r', encoding="utf-8") as f:
    modify_test_test = json.load(f)
print(modify_test_test[0])
print('\n---test json modify successfully---')