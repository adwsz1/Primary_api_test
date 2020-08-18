#! /bin/bash
if [ ! -d "./venv/" ]; then

    python3.8 -m venv ./venv/
    . venv/bin/activate
    pip install -r requirements.txt

else

    echo "文件夹已经存在"

fi

hrun ./testcases/ --alluredir=allure-results/
