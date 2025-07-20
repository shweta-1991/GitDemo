import pytest


@pytest.mark.usefixtures("setup")
class Test:
    def test_setuptest(self,setup):
        print("test_setuptest in class")
        print(setup)

