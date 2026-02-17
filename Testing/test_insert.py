from Pipelines.ingest import ingest
from Pipelines.evaluate import evaluate
from Pipelines.insert import insert

# Chess.com username
USERNAME = 'kingsk4'

# Ingestion
meta_df, move_df = ingest(USERNAME, start_date='2024-02', end_date='2024-02')

# Evaluation
eval_df = evaluate(move_df, depth=8, username=USERNAME)

# Database insertion
insert(meta_df,eval_df,username=USERNAME)