import pytest
@pytest.mark.parametrize("num,output",[(1,1),(2,4),(3,27),(4,256)])
def test_factorial(num,output):
 factorial=1
 for i in range(1,num+1):
  factorial=factorial*num
 assert factorial==output