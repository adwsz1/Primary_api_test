# NOTE: Generated By HttpRunner v3.1.4
# FROM: har/0806获取验证码.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0806获取验证码(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/passport/sendCaptcha")
            .post(
                "https://api-primary.yangcong345.com/primary_account/passport/sendCaptcha"
            )
            .with_headers(
                **{
                    "content-length": "257",
                    "accept": "application/json, text/plain, */*",
                    "x-crypto-api": "true",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://yangcong345.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://yangcong345.com/xiaoxue/login",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json(
                {
                    "sign": "FAA84E43443689F9112B396E011EDA5B5F2B858Aprimary",
                    "context": "VTJGc2RHVmtYMTlJOVZEakxqVkp3QUxYQnNMTzJJaFYwcG5HejVOd1BlWWNlQy9ybTB3RXdOc0xsN0tlZWlUTkQrSXFJTGtqMmRzaUZyMTZHM09vbTc3Mzk3Z2RxOWd2MVpvNFdlbmdrZ1BhbnI3cUd0Y2NEbHF0elhtNURjWHc=",
                    "crypto": True,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                "body.sign", "5B40099F45B3EABFB4F5685F118977E05F2B858Aprimary"
            )
            .assert_equal(
                "body.context",
                "VTJGc2RHVmtYMStzZ2pFb1BGdEcwRkJQK0dKOElvOFBoeFVjR3JMMFJzUFF0S0h6Q0QvallQZVdYeVBrTzh1OVMxSStJaTEvVEpzc2t0aStrUVYzOHc9PQ==",
            )
            .assert_equal("body.crypto", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseT0806获取验证码().test_start()
