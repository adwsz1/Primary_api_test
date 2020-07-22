# NOTE: Generated By HttpRunner v3.1.3
# FROM: har/获取h5用户token.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase获取H5用户Token(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/passport/appH5AuthToken")
            .post(
                "https://api-wx.yangcong345.com/primary_account/passport/appH5AuthToken"
            )
            .with_headers(
                **{
                    "content-length": "597",
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://h5-v5-0.yangcong345.com",
                    "x-crypto-api": "true",
                    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; vmos Build/LMY48G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
                    "content-type": "application/json;charset=UTF-8",
                    "referer": "https://h5-v5-0.yangcong345.com/xs-app/?userId=5ebb670226002e00017e470d&token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjVlYmI2NzAyMjYwMDJlMDAwMTdlNDcwZCIsInJvbGUiOiJzdHVkZW50IiwiaWF0IjoxNTkyMzgyMDQyLCJleHAiOjE1OTYyNDk3Mjl9.YYA2WILeL6zl42JA1xtaJB_8hnJdNty1SVcrpPBiq9Q&device=fcf6c66211e195fd&platform=android&exerciseDebug=0&clientType=android-app&appVersion=5.29.0&clientChannel=yangcong&environment=release&appCategory=student&phoneModel=vmos&channel=yangcong&env=prod",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "zh-CN,en-US;q=0.8",
                    "x-requested-with": "com.yangcong345.android.phone",
                }
            )
            .with_json(
                {
                    "sign": "BB1BF5468BE2D01E03DAFBE23BA0B3FD5EFED3C3primary",
                    "context": "VTJGc2RHVmtYMTg2OXNmOFFib1htbnBDNERLMVlyNVlyTkNXanVyYzFhbWNOcHFkaFZ1YlNxNklqZGpTNjBDRmR5QWovUTRHQUJYdmhycTQxNDFMYlRFYzVvcnAvTndKaTJNdzVhbm1BUHBXbExEQ0VyaGJQNllCajZpdUNIRVA2Q1FmZDlnL2ErSUZrRnpnaENybnF2ZGZycGhac0lQYUFSa01Jd0JhWnR6Yi9meWZ1OTJNMUs5YXpzSlNTQkdueG1TMmVhTEZ4anZzWkhOZ1hXQUxQdFdOQmhTbU5mVUtIKzRpQmNtMFVLOC9KYm9ySGRqeERWOXJJdmNIRlQyaVRMTDhHcjRHSTlPVnNiZ3RFRU15V04rNmQrUWZMblZJbGtKbzNhOUNsTHNZQ25XVEJNNitvZ3RBRzlFVzNXTkpGRzhwNjBsaXBWQndxTFlYOGsrZGJmaUpsMXRZUFF2MEpEd0t2Z2JuY1cvUFRXNEJ6SWE1aUtJZVgwVDh4K25P",
                    "crypto": True,
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.crypto", True)
        ),
    ]


if __name__ == "__main__":
    TestCase获取H5用户Token().test_start()
