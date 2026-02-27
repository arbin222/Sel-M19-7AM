def test_sadaf():
    print("it is test_fourth")

class TestSample:
    cname='Arbin'
    def test_one(self):
        print("class test case 1")

    def test_two(self):
        assert self.cname==self.cname[::-1], "Cname is not palindrome"
        print("It is a palindrome")
