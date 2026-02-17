from Pipelines.ingest import ingest
from Pipelines.evaluate import evaluate

_, move_df = ingest('kingsk4','2026-02','2026-02')

print('PRE-EVALUATION')
print(move_df.head(7))

eval_df = evaluate(move_df)

print('POST-EVALUATION')
print(eval_df.head(7))