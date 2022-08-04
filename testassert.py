import mathlib123

def testcalsquare1():
    result = mathlib123.cal_square(5)
    assert result==25


def testcalsquare2():
    result = mathlib123.cal_square(7)
    assert result == 50

def  calsquare3():
    result = mathlib123.cal_square(8)
    assert result == 64

def testcalsquare4():
    result = mathlib123.cal_square(9)
    result -== 81