import pandas as pd # type: ignore
pd.set_option('display.max_rows', 5)

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
# print(wine_reviews.shape)
# print(wine_reviews.head())
print(wine_reviews)

# SELECTING IN PANDAS

# Neither of them is more or less syntactically valid than the other, but the indexing operator [] 
# does have the advantage that it can handle column names with reserved characters in them

print("\nThere are the two ways of selecting a specific Series out of a DataFrame:")
print(wine_reviews.country) # attribute
print(wine_reviews['country']) # dictionary
print("\nWe can also select a specific value:\n{}".format(wine_reviews['country'][0]))

# INDEXING IN PANDAS

# Index-based selection means selecting data based on its numerical position in the data. iloc follows this paradigm.
print("\nTo select the first row of data in a DataFrame:\n{}".format(wine_reviews.iloc[0]))
# Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.
print("\nTo select the first column of data in a DataFrame:\n{}".format(wine_reviews.iloc[:, 0]))
print("\nTo select the first three rows and first three columns:\n{}".format(wine_reviews.iloc[0:3, 0:3]))
print("\nOr, to select just the second and third entries, we would do:\n{}".format(wine_reviews.iloc[1:3, 0]))
print("\nIt's also possible to pass a list:\n{}".format(wine_reviews.iloc[[0, 2, 5], 0]))
print("\nFinally, it's worth knowing that negative numbers can be used in selection\n{}".format(wine_reviews.iloc[-5:]))

# With the second paradigm, it's the data index value, not its position, which matters.
print("\nTo get the first entry in wine_reviews, we would now do:\n{}".format(wine_reviews.loc[0, 'country']))
print(wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])
# iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
# So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.