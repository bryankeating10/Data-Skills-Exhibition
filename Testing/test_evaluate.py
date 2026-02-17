from Pipelines.ingest import ingest
from Pipelines.evaluate import evaluate

# USERNAME
USERNAME = 'bkchessmaster2'
_, move_df = ingest(USERNAME, start_date='2026-01', end_date='2026-02')

print('PRE-EVALUATION')
print(move_df.head(7))

eval_df = evaluate(move_df, depth=25, username=USERNAME)

print('POST-EVALUATION')
print(eval_df.head(7))