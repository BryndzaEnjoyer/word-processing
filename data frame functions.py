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
