httprunner startproject primary_api_test    
har2case    
hrun har/test_har_test.py --alluredir=alluredir_reports/

pip install -r requirements.txt

.   
├── README.md   
├── __pycache__ 
│   └── debugtalk.cpython-38.pyc    
├── alluredir_reports   
│   ├── 7bfd6976-fc3b-4163-b443-2ce1f150a741-attachment.txt
│   ├── 8ef5bb5f-2798-49f1-9704-25a5d3ffa0f9-attachment.txt
│   ├── ab177e42-a93b-4a99-91bc-075dad006c44-result.json
│   └── b3733bd2-3b86-4c40-b45e-a3bda2c430a3-result.json
├── debugtalk.py
├── har
├── logs
│   ├── c2a27a81-3d2c-4032-b280-e98a44d9ad55.run.log
│   └── fcfdbe3c-1b44-430b-977f-38628f1c14a2.run.log
├── reports
├── requirements.txt
└── testcases
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   ├── demo_testcase_ref_test.cpython-38-pytest-5.4.3.pyc
    │   └── demo_testcase_request_test.cpython-38-pytest-5.4.3.pyc
    ├── demo_testcase_ref.yml
    ├── demo_testcase_ref_test.py
    ├── demo_testcase_request.yml
    └── demo_testcase_request_test.py
