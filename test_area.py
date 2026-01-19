from area import area_cicumference
import math

def test_areacase():
    assert area_cicumference(5) == f"Radius : 5\nArea : {math.pi*25}\nCircumference : {2*math.pi*5}"
    
