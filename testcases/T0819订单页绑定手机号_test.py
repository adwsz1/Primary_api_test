# NOTE: Generated By HttpRunner v3.0.12
# FROM: har/0819订单页绑定手机号.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0819订单页绑定手机号(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/passport/appH5Auth")
            .post(
                "https://api-primary.yangcong345.com/primary_account/passport/appH5Auth"
            )
            .with_headers(
                **{
                    "content-length": "289",
                    "origin": "https://yangcong345.com",
                    "x-crypto-api": "true",
                    "authorization": "",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json",
                    "user-agent": "Mozilla/5.0 (Linux; Android 9; V1813BT Build/PKQ1.181030.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.1.14.2",
                    "referer": "https://yangcong345.com/pg/p/order?classType=0&enrollmentAgentId=&planId=131&grade=3&publisherId=1&classStartTime=2020-09-03T16%3A00%3A00.000Z&classEndTime=2020-09-07T16%3A00%3A00.000Z&planDetailId=572&goodsId=5f34e498af3158758f3d229a&ycfrom=xsapp-1",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,en-US;q=0.9",
                }
            )
            .with_json(
                {
                    "sign": "2E76677387BE4BF7C15DC3F9BD6C27085F3CCFE1primary",
                    "context": "VTJGc2RHVmtYMSsvUU9EeVBqNHBoM3dCZEhyTTF0OW5Yb0pyc0IzbmFpdTJCNTBrWEMwUU1vUjFDTEpDSllHM3ZDTTlxTVRFSWYwWVdyOVV3bG5SWEJrY0VDeGdDRncrTlBUTkdSQXY3UjQybmpHOGpIaDRaWFBWVGJEVFZzWTRmS2M0V3pqNm9NZFlLRWY2elN1WGFRPT0=",
                    "crypto": True,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                "body.sign", "00D9D0E9AD00C282B99A1A49CF42E7E15F3CCFDEprimary"
            )
            .assert_equal(
                "body.context",
                "VTJGc2RHVmtYMStiZGk1WXNyaVlyOEVuSEpxRUJQc3dqNUdXK0JBU1puV2trck9uV1NpTjBXNWc1OVhKcTNGQXJ4TTV5VFFjYnkraHBWUzlzSnhuR0VrNUFrYWRkRHQ5QksxVG9xRzBhSDdCeS9KYnc0RVpjSGdwZUpNeXJEWnVkOFBVVUl4eUlQWTQzSTNCb3BoaUlhbG5admtuRFdrcnFnaE9DbDhOVG9zR1FaRWNwRFNrVnBVUk51Q253aW5XOUlRMklLSmRGaGVsVGIwcklsTDBIek9uZUU3emdwTU11STVrMkk1L2U5am9Sd0lpRElDZktYNGJ0a0tMKzg4czVUV1JoVVN4Y3dWQmsxRGpkdDNVNjIrQlRvUjMrQnA0dzNnNmJOclh6ay9uRUNzZzNjTWlrZVVhZDBCZG5DUjRyVzhPbkhvbjhTV095bnVEWW50OEx2YTF5VlJKdjZMRytKclUyRnZZTFZHRDBHYlVrMlQvbXNMMWlBSDVERHdCTVV2S0g0M2VDeHJUb0orT2VnR0FsUT09",
            )
            .assert_equal("body.crypto", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseT0819订单页绑定手机号().test_start()
