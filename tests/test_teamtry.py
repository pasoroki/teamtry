from teamtry import main


class TestTeamtry:
    """
    High level tests
    """

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
        result = main()
        assert result == 0, "Main must always return 0"
