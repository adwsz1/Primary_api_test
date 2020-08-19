# NOTE: Generated By HttpRunner v3.0.12
# FROM: har/0819是否支付成功，发货成功信息.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0819是否支付成功_发货成功信息(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        
            Step(RunRequest("/primary_account/commodity/queryPrePayCommodity").post("https://api-primary.yangcong345.com/primary_account/commodity/queryPrePayCommodity").with_headers(**{'content-length': '46', 'accept': 'application/json', 'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJ5aWQiOiI1ZGMyODY1MDFlODZmMDBmNWY0OWZiNjciLCJwaG9uZSI6IjE4NDA0OTEyNzY5IiwicGxhdGZvcm0iOiJ1bmtub3duIiwid2VjaGF0SWQiOjM3MzM4NSwiZXhwIjoxNjI4NjEyMTY2fQ.ozxQjBeVxEEuxykRMiis_RM22lG_4Y21lb0LJSHtJPI', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://yangcong345.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://yangcong345.com/pg/p/confirm?ycfrom=xsapp-1&enrollmentAgentId=&prePayCommodityId=023b24db-4385-423d-99c6-72df11c60211&subject=undefined&orderId=5f3ccea486b7163c7d064a12', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9'}).with_json({'platformOrderId': '5f3ccea486b7163c7d064a12'}).validate().assert_equal("status_code", 200)),
        
    ]

if __name__ == "__main__":
    TestCaseT0819是否支付成功_发货成功信息().test_start()
