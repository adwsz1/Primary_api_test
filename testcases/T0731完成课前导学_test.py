# NOTE: Generated By HttpRunner v3.1.3
# FROM: har/0731完成课前导学.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0731完成课前导学(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest(
                "/primary_account/video-manager/videos/5f1eb3c85eddaa3731129ef8/learn-report"
            )
            .put(
                "https://api-wx.yangcong345.com/primary_account/video-manager/videos/5f1eb3c85eddaa3731129ef8/learn-report"
            )
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://h5-v5-0.yangcong345.com",
                    "content-type": "application/json;charset=utf-8",
                    "authorization": "eyJhbGciOiJIUzI1NiJ9.eyJ5aWQiOiI1ZTNhZmJkNWFmNjU0ODAwMDFjZTIyOTgiLCJwaG9uZSI6IjE4NTI0NjM1MjI3IiwicGxhdGZvcm0iOiJhcHBMZWFybkg1Iiwid2VjaGF0SWQiOjE5NTIzMSwiZXhwIjoxNjI3NzIzMzM4fQ.xRItRjFdVoKqKsU8dMQoPLoxod8uUGsli0Jf9VSsoGo",
                    "referer": "https://h5-v5-0.yangcong345.com/xs-app/cv2/lessonInfo",
                    "content-length": "144",
                    "accept-language": "zh-cn",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko)",
                    "accept-encoding": "gzip, deflate, br",
                    "Postman-Token": "f4e06caf-d09e-4a86-be9e-b4ac88ca85aa",
                    "Host": "api-wx.yangcong345.com",
                    "Connection": "keep-alive",
                }
            )
            .with_json(
                {
                    "played": 765,
                    "lessonId": "5f07dfe810951330d09acbec",
                    "classId": "5f0dbf98e08ce80fd5fa97d7",
                    "moduleId": "5f1fdba2d9041f8eb60a3f9b",
                    "platform": "app",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; charset=utf-8")
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseT0731完成课前导学().test_start()
