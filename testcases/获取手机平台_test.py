# NOTE: Generated By HttpRunner v3.1.2
# FROM: har/获取手机平台.har

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase获取手机平台(HttpRunner):
    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/primary_account/passport/getPlatformPhone")
            .get(
                "https://api-wx.yangcong345.com/primary_account/passport/getPlatformPhone"
            )
            .with_params(
                **{
                    "sign": "1CAB196BA46FF4B1F229C75D023BE5925EFED3C0primary",
                    "context": "VTJGc2RHVmtYMTg3QlNpK3Q2YjVTNFVjTkVGaG9yNkc2L1Q5VU96WGUzYlA1TjdBYVpHdmE4eS9lTVYyYmM2UzY1dlhGbWVudThsUHdkdnd4MllEeFp1V2N6RXhHVWNDZEJ5eklZUVZKMmxza1JBcUFhd0IvMU9RaElDbjlDNDIrdmY0Y1RjeU9qb0l5anpqT0NDTjR6SGdEVGpHNHlqSW5tTUd3NzZGM21sMWl3SStPK1A5Q1FPZndvdU04eGJ0SGx1K0xZa1M3S3UrM3grQ2hTY1hwRjNkcUJqd3M0Z1BNUUo0YjcwRUdDcFNXU0g1MW5nRlAxWUhCUmdUTkZ3bzd3WmJNZkZYK2tOODhCNkFRb0lpSzZ0NG9lVDFGSUIyTXV2OWxTdHhoSFRLRzdIMGZTditPUDNuSGVCVURySmdpWVZnNXRXbHRobFhvUkRELytPVTJ6OU1MdlloaFgwN1RLNnI0SnQzR2xNPQ==",
                    "crypto": "true",
                }
            )
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "origin": "https://h5-v5-0.yangcong345.com",
                    "x-crypto-api": "true",
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
    TestCase获取手机平台().test_start()
