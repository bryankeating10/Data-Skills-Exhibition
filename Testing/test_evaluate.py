from Pipelines.ingest import ingest
from Pipelines.evaluate import evaluate

# Chess.com username and time frame
USERNAME = 'noahjaskiewicz'
START_DATE = '2020-09'
END_DATE = '2020-09'

# Ingest
_, move_df = ingest(USERNAME, start_date='2020', end_date='2026-02')

print('PRE-EVALUATION')
print(move_df.head(7))

# Evaluate
eval_df = evaluate(move_df, depth=8, username=USERNAME)

print('POST-EVALUATION')
print(eval_df.head(7))