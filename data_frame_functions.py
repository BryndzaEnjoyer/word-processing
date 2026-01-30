import pandas as pd

data={
    "A": [1, 2, 3],
    "B": [4, 5, 6],
}
df = pd.DataFrame(data)

def read_collumn(collumn):
    return df[collumn]
A=read_collumn("A")
B=read_collumn("B")

summation = A.add(B,fill_value=0)
def summation(A,B):
    sum = A.add(B,fill_value=0)
    return sum
def division(A,B):
    division = A.div(B,fill_value=0)
    return division
def multiplicantion(A,B):
    multiplication = A.mul(B,fill_value=0)
    return multiplication
def substraction(A,B):
    subtraction = A.sub(B,fill_value=0)
    return subtraction
def sumandmultiplication(sum,multiplication):
    sum = A.add(B,fill_value=0)
    sumandmultiplication= sum*2
    return sumandmultiplication

sumandmultiplication_result = sumandmultiplication(summation,2)
print(sumandmultiplication_result)