import json
import sys
import numpy as np
import torch
from torch.utils.data import DataLoader
from transformers import pipeline, AutoTokenizer, AutoModelForMultipleChoice,AutoModelForQuestionAnswering
import pandas as pd
import os

# load path
context_path = sys.argv[1]
print("context_path:", context_path, '\n')
test_path = sys.argv[2]
print("test_path:", test_path, '\n')
prediction_path = sys.argv[3]
print("prediction_path:", prediction_path, '\n')


# Load test datasets and pre-trained model
with open('./2023ADLHW1/json/modify_test_Paragraph.json', 'r', encoding="utf-8") as f:
    test_dataset = json.load(f)
Paragraph_tokenizer = AutoTokenizer.from_pretrained("./2023ADLHW1/pretrained_model/Titan_1012_macbertbaseBatch2Epoch1Total_Paragraph")
Paragraph_model = AutoModelForMultipleChoice.from_pretrained("./2023ADLHW1/pretrained_model/Titan_1012_macbertbaseBatch2Epoch1Total_Paragraph")
QA_model = pipeline("question-answering", model="./2023ADLHW1/pretrained_model/Titan_1011_lertlargeBatch8Epoch3Length512Total_QA", device=0 if torch.cuda.is_available() else -1)

# Inference
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
Paragraph_model.eval()
Paragraph_model.to(device)
column_labels = ['id', 'answer']
submission_df = pd.DataFrame(columns=column_labels)
for step, batch in enumerate(test_dataset):
    # Select paragraph
    prompt = batch['sent1']
    candidate0 = batch['ending0']
    candidate1 = batch['ending1']
    candidate2 = batch['ending2']
    candidate3 = batch['ending3']
    inputs = Paragraph_tokenizer([[prompt, candidate0], [prompt, candidate1], [prompt, candidate2], [prompt, candidate3]], return_tensors="pt", padding=True, truncation=True, max_length=512)
    inputs.to(device)
    with torch.no_grad():
        outputs = Paragraph_model(**{k: v.unsqueeze(0) for k, v in inputs.items()})
    logits = outputs.logits
    predicted_class = logits.argmax().item()

    # extract answer
    question = prompt
    context = batch[f'ending{predicted_class}']
    ans = QA_model(question=question, context=context)

    # store
    new_row = {'id':batch['id'], 'answer':ans['answer']}
    submission_df = pd.concat([submission_df, pd.DataFrame([new_row])], ignore_index=True)
    
    # monitor
    print('----------------------')
    print(batch['sent1'])
    print(ans['answer'])
    print(f'{step+1}/{len(test_dataset)}')

# Save as csv
submission_df.to_csv(prediction_path,index=False)
print(f'pred save at :{prediction_path}')
