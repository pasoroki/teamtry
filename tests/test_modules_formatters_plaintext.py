from modules.formatters.plaintext import Formatter_PlainText


class TestParserPlainText:
    """
    High level tests
    """
    formatter = Formatter_PlainText()

    def setup_class(self):
        print("\nSETUP class\n")

    def teardown_class(self):
        print("\nTEAR DOWN class\n")

    def test_empty_test(self):
        """
        Just for test. Delete when other tests start working
        """
        pass

    def test_main__just_a_test__returns_0(self):
        """
        Just for test. Delete when other tests start working
        """
        data = {
                  "dateCreated": "2018-11-06T21:20:08.143Z",
                  "events": [
                    "event.alert",
                    "event.created"
                  ],
                  "id": "4f9d73e63b7144ecb8944c41620a090b",
                  "secret": "8fcac28aaa4c4f5fa572b61d40a8e084364db25fd37449c299e5a41c0504cbc2",
                  "status": "active",
                  "url": "https://example.com/sentry-hook"
                }

        result = self.formatter.process(data=data)
        print(f"\n\nFinal result: {result}\n")
        assert result == 0, "Main must always return 0"
