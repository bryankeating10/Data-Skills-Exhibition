from Pipelines.ingest import ingest
from Pipelines.evaluate import evaluate

# Chess.com username and time frame
o1 = ['bkchessmaster2','2026-01','2026-02']
o2 = ['noahjaskiewicz', '2020-09','2020-09']

USERNAME = o2[0]
START_DATE = o2[1]
END_DATE = o2[2]

# Ingest
_, move_df = ingest(USERNAME, START_DATE, END_DATE)

print('PRE-EVALUATION')
print(move_df.head(7))

# Evaluate
eval_df = evaluate(move_df, depth=8, username=USERNAME)

print('POST-EVALUATION')
print(eval_df.head(7))