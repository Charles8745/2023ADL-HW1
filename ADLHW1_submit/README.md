
# ADL HW1: m11203404 陳旭霖
以下內容包含:
* Build up environment
* Download models and data
* Preprocess and Inference
* Training 
* Contact Information

## Build up environment
- Step1: Please create and activate your venv first
- Step2: install torch
    ```
    pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
    ```
- Step3: install requirement.txt 
    ```
    pip install -r requirement.txt
    ```

## Download models
- Option1: Download by Shell Scripts
    ```
    bash ./download.sh
    ```
- Option2: Download 2023ADLHW1_gDrive.zip by gDrive: 
    
    https://drive.google.com/file/d/1fb7_athHmHgl9j7f_PSj7K69_ixZS7XH/view?usp=drive_link

## Preprocess and Inferance
- Execute by Shell Scripts
    ```
    bash ./run.sh /path/to/context.json /path/to/test.json /path/to/pred/prediction.csv
    ```
## Training
- Step1: 先將作業提供的json檔案修改成程式可以讀取的格式
    ```
    python modify_train+valid.py # 將train與valid合成為一個訓練json

    python modify_Paragraph_json.py # 修改test、valid

    python modify_QA_json.py # 修改test、valid

    python modify_test_json.py # 修改test
    ```

- Step2: 訓練Paragraph
    ```
    python run_swag_no_trainer.py --model_name_or_path bert-base-chinese --train_file   modify_total_Paragraph.json --validation_file modify_valid_Paragraph.json --max_seq_length 512 --per_device_train_batch_size 4 --learning_rate 3e-5 --num_train_epochs 1 --output_dir /xxxx/xxxx/
    ```

- Step3: 訓練QA
    ```
    python run_qa_no_trainer.py --train_file modify_total_QA.json --validation_file modify_valid_QA.json --max_seq_length 512 --model_name_or_path bert-base-chinese --per_device_train_batch_size 8 --learning_rate 3e-5 --num_train_epochs 3 --output_dir /XXX/XXX/ 

    ```

- Step4: Inference. 記得修改裡面讀取模型的路徑
    ```
    python Inference.py
    ```

## Contact
- Email: charles77778888asd@gmail.com 
- linkedin: www.linkedin.com/in/旭霖-陳-b34102277





