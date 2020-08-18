# NOTE: Generated By HttpRunner v3.0.12
# FROM: har/0818增加葱钻.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseT0818增加葱钻(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/shadow/handleUserWallet")
            .post(
                "https://api-primary.yangcong345.com/primary_account/shadow/handleUserWallet"
            )
            .with_headers(
                **{
                    "content-length": "126",
                    "accept": "application/json",
                    "shadowauthorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVjMDc0NzM3MTdjNTRiMDVhZGI1NWViNSIsImlhdCI6MTU5NzI5OTM3NywiZXhwIjoxNTk4NTA4OTc3fQ.0J0zdg5ZbsS3oLjNpfxXn-X20jVfPws5EMwNQfX9W9E",
                    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVjMDc0NzM3MTdjNTRiMDVhZGI1NWViNSIsImlhdCI6MTU5NzI5OTM3NywiZXhwIjoxNTk4NTA4OTc3fQ.0J0zdg5ZbsS3oLjNpfxXn-X20jVfPws5EMwNQfX9W9E",
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "origin": "https://yangcong345.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://yangcong345.com/admin/dimand/manage",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json(
                {
                    "type": "income",
                    "mount": 1,
                    "extra": "自动化测试",
                    "userId": "5e3afbd5af65480001ce2298",
                    "classId": "5f23e7414b246b32da120c62",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.result", True)
        ),
    ]


if __name__ == "__main__":
    TestCaseT0818增加葱钻().test_start()
