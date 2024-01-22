import pandas as pd

df = pd.read_csv("/Users/ayushbansal/Code ay/MTP-II/nodes.csv")
node_id = pd.DataFrame(df, columns=['id'])
print(node_id)