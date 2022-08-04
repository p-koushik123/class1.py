import pytest
@pytest.mark.parametrize("num,output",[(1,1),(2,3),(3,6),(4,10)])
def test_sum_of_naturals(num,output):
 sum=0
 for i in  range(num+1):
     sum=sum+i
 assert sum==output