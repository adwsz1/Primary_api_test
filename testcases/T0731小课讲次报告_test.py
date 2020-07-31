# NOTE: Generated By HttpRunner v3.1.3
# FROM: har/0731小课讲次报告.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0731小课讲次报告(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/learnReport/lesson-report")
            .get(
                "https://api-wx.yangcong345.com/primary_account/learnReport/lesson-report"
            )
            .with_params(
                **{
                    "platform": "app",
                    "classId": "5f0dbf98e08ce80fd5fa97d7",
                    "moduleId": "5f07dfe810951339519acbef",
                    "lessonId": "5f07dfe810951356079acbee",
                }
            )
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://h5-v5-0.yangcong345.com",
                    "referer": "https://h5-v5-0.yangcong345.com/xs-app/cv2/lessonReport",
                    "accept-language": "zh-cn",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko)",
                    "authorization": "eyJhbGciOiJIUzI1NiJ9.eyJ5aWQiOiI1ZTNhZmJkNWFmNjU0ODAwMDFjZTIyOTgiLCJwaG9uZSI6IjE4NTI0NjM1MjI3IiwicGxhdGZvcm0iOiJhcHBMZWFybkg1Iiwid2VjaGF0SWQiOjE5NTIzMSwiZXhwIjoxNjI3NzIzMzM4fQ.xRItRjFdVoKqKsU8dMQoPLoxod8uUGsli0Jf9VSsoGo",
                    "accept-encoding": "gzip, deflate, br",
                    "Postman-Token": "40892544-d360-4b48-8e10-b42ab92267e3",
                    "Host": "api-wx.yangcong345.com",
                    "Connection": "keep-alive",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; charset=utf-8")
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseT0731小课讲次报告().test_start()
