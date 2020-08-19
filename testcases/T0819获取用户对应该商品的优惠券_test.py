# NOTE: Generated By HttpRunner v3.0.12
# FROM: har/0819获取用户对应该商品的优惠券.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0819获取用户对应该商品的优惠券(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest(
                "/primary_account/coupon/user/coupon/getUserCouponsSortByGoodsId"
            )
            .get(
                "https://api-primary.yangcong345.com/primary_account/coupon/user/coupon/getUserCouponsSortByGoodsId"
            )
            .with_params(
                **{
                    "userId": "5dc286501e86f00f5f49fb67",
                    "goodsId": "5f34e498af3158758f3d229a",
                }
            )
            .with_headers(
                **{
                    "authorization": "eyJhbGciOiJIUzI1NiJ9.eyJ5aWQiOiI1ZGMyODY1MDFlODZmMDBmNWY0OWZiNjciLCJwaG9uZSI6IjE4NDA0OTEyNzY5IiwicGxhdGZvcm0iOiJ1bmtub3duIiwid2VjaGF0SWQiOjM3MzM4NSwiZXhwIjoxNjI4NjEyMTY2fQ.ozxQjBeVxEEuxykRMiis_RM22lG_4Y21lb0LJSHtJPI",
                    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                    "accept": "*/*",
                    "origin": "https://yangcong345.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://yangcong345.com/pg/p/order?classType=0&enrollmentAgentId=&planId=131&grade=3&publisherId=1&classStartTime=2020-09-03T16%3A00%3A00.000Z&classEndTime=2020-09-07T16%3A00%3A00.000Z&planDetailId=572&goodsId=5f34e498af3158758f3d229a&ycfrom=xsapp-1",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseT0819获取用户对应该商品的优惠券().test_start()
