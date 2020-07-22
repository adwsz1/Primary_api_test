# NOTE: Generated By HttpRunner v3.1.2
# FROM: har/获取用户信息.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase获取用户信息(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/passport/getUserInfo")
            .get("https://api-wx.yangcong345.com/primary_account/passport/getUserInfo")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://h5-v5-0.yangcong345.com",
                    "authorization": "eyJhbGciOiJIUzI1NiJ9.eyJ5aWQiOiI1ZWJiNjcwMjI2MDAyZTAwMDE3ZTQ3MGQiLCJwbGF0Zm9ybSI6ImFwcExlYXJuSDUiLCJ3ZWNoYXRJZCI6MzUyNDQwLCJleHAiOjE2MjUyOTQ2NjF9.l8q8jEwYqYt2FKkQIVXPf-tCFeWkw6A9C-1TyS1Z8Gw",
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; vmos Build/LMY48G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
                    "referer": "https://h5-v5-0.yangcong345.com/xs-app/tab/goods",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "zh-CN,en-US;q=0.8",
                    "x-requested-with": "com.yangcong345.android.phone",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCase获取用户信息().test_start()
