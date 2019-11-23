import pandas as pd
df = pd.read_csv("election_data.csv")
total_num_votes =df["voter id"].shape[0]
count_df = df.groupby("candidate").count()[["voter id"]].assign(proportion=lambda df:["voter id"] / total_num_votes)
print(count_df)