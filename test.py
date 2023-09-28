import pandas as pd
def df_to_csv(input_df,path):
  input_df.to_csv(f"{path}/New_file.csv",index=False)
