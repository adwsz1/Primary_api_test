# Primary_api_test
洋葱apitest
环境：```python3.8``` ```httprunner3.1.4```

建议使用virtual环境运行：```python3.8 -m venv ./venv/```
激活virtual环境：```. venv/bin/activate```
安装项目依赖：```pip install -r requirements.txt```

使用httprunner脚手架搭建：```httprunner startproject primary_api_test```

将charles导出的har转换为yaml或json或pytest文件：```har2case```    

跑case时使用命令，使用了allure-pytest报告插件：```hrun har/test_har_test.py --alluredir=alluredir_reports/```

如果需要本地运行allure报告，请先安装allure本地客户端，allure-pytest报告服务启动：```allure serve alluredir_reports/```

项目结构说明
```
.
├── README.md
├── alluredir_reports  #在使用allrue-pytest插件生成报告存放到此处
├── debugtalk.py  #在运行case时使用的插件
├── har  #存放charles导出的har文件
├── logs  #hrun后生成的日志
    ├── *.log
├── reports  #httprunner自带日志报告输出
├── requirements.txt  #项目依赖
└── testcases    #测试case存放处，可存放yaml、json、pytest
    ├── *.yml
    ├── *.py
    ├── *.json
└── .env    #存放环境变量
```

dos2unix file
