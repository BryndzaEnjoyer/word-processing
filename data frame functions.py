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

sum = A.add(B,fill_value=0)
division = A.div(B,fill_value=0)
multiplication = A.mul(B,fill_value=0)
subtraction = A.sub(B,fill_value=0)
def sumandmultiplication(sum,multiplication):
    sumandmultiplication = sum.mul(multiplication,fill_value=0)
    return sumandmultiplication

sumandmultiplication_result = sumandmultiplication(sum,2)
print(sumandmultiplication_result)