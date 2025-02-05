import pandas as pd
file_path = 'C:\Users\sures\OneDrive\Desktop\Swati\Invoices\my\data-engineer-assignment\references_log.jsonl'

df = pd.read_json(file_path, lines=True)
print(df)
