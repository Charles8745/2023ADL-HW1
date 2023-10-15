import json
import numpy as np
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForMultipleChoice,AutoModelForQuestionAnswering

rad_idx = np.random.randint(0,399)
# Load one Multi-choose 
with open('modify_test_Paragraph.json', 'r', encoding="utf-8") as f:
    modify_valid_test_Paragraph = json.load(f)

# Inference 
prompt = modify_valid_test_Paragraph[rad_idx]['sent1']
candidate0 = modify_valid_test_Paragraph[rad_idx]['ending0']
candidate1 = modify_valid_test_Paragraph[rad_idx]['ending1']
candidate2 = modify_valid_test_Paragraph[rad_idx]['ending2']
candidate3 = modify_valid_test_Paragraph[rad_idx]['ending3']

tokenizer = AutoTokenizer.from_pretrained("Titan_1004_BertchineseBatch2Epoch1_test")
model = AutoModelForMultipleChoice.from_pretrained("Titan_1004_BertchineseBatch2Epoch1_test")

inputs = tokenizer([[prompt, candidate0], [prompt, candidate1], [prompt, candidate2], [prompt, candidate3]], return_tensors="pt", padding=True, truncation=True, max_length=512)

with torch.no_grad():
    outputs = model(**{k: v.unsqueeze(0) for k, v in inputs.items()})
logits = outputs.logits
predicted_class = logits.argmax().item()

#qa
question = prompt
context = modify_valid_test_Paragraph[rad_idx][f'ending{predicted_class}']
question_answerer = pipeline("question-answering", model="Titan_1006_chineseBatch8Epoch1Length512_QA")
ans = question_answerer(question=question, context=context)

print(modify_valid_test_Paragraph[rad_idx][f'ending{predicted_class}'])
print('----------------------')
print(modify_valid_test_Paragraph[rad_idx]['id'])
print(modify_valid_test_Paragraph[rad_idx]['sent1'])
print(ans['answer'])



