# NOTE: Generated By HttpRunner v3.1.2
# FROM: har/用户课程.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase用户课程(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/course/userCourse")
            .get("https://api-wx.yangcong345.com/primary_account/course/userCourse")
            .with_params(
                **{
                    "sign": "46375D862CD5B645C7187B6C1820567D5EFED3C5primary",
                    "context": "VTJGc2RHVmtYMTl2TjE3WlpVRWFPelRCcUVWbnJkd0swcVUyd2dQNXNzN2VYcmlNcm1uWngrbTdqVkVXMk1paGFkNzVQYldudU9pMmIwdzEwd2o5NktMWG9xNzg0bW84aUg1aXdlYjcyZWM9",
                    "crypto": "true",
                }
            )
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://h5-v5-0.yangcong345.com",
                    "x-crypto-api": "true",
                    "authorization": "eyJhbGciOiJIUzI1NiJ9.eyJ5aWQiOiI1ZWJiNjcwMjI2MDAyZTAwMDE3ZTQ3MGQiLCJwbGF0Zm9ybSI6ImFwcExlYXJuSDUiLCJ3ZWNoYXRJZCI6MzUyNDQwLCJleHAiOjE2MjUyOTQ2NjF9.l8q8jEwYqYt2FKkQIVXPf-tCFeWkw6A9C-1TyS1Z8Gw",
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; vmos Build/LMY48G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
                    "referer": "https://h5-v5-0.yangcong345.com/xs-app/?userId=5ebb670226002e00017e470d&token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVlYmI2NzAyMjYwMDJlMDAwMTdlNDcwZCIsInJvbGUiOiJzdHVkZW50IiwiaWF0IjoxNTkyMzgyMDQyLCJleHAiOjE1OTYyNDk3Mjl9.YYA2WILeL6zl42JA1xtaJB_8hnJdNty1SVcrpPBiq9Q&device=fcf6c66211e195fd&platform=android&exerciseDebug=0&clientType=android-app&appVersion=5.29.0&clientChannel=yangcong&environment=release&appCategory=student&phoneModel=vmos&channel=yangcong&env=prod",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "zh-CN,en-US;q=0.8",
                    "x-requested-with": "com.yangcong345.android.phone",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.crypto", True)
        ),
    ]


if __name__ == "__main__":
    TestCase用户课程().test_start()
