def multiplies_two_numbers(a: int,b:int) -> int:
    assert isinstance(a,int), "Multiplies of numbers must be type INT"
    #assert all(isinstance(arg,(int)) for arg in [a,b]), "a or b must be int to multiplie two numbers"
    return a * b 
