import pandas as pd

df = {
    'name':['Ram','Sam'],
    'ages':[78,61]
}

db = pd.DataFrame(df)

print(db)