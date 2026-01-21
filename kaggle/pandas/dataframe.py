import pandas as pd # type: ignore
pd.set_option('display.max_rows', 5)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(df)