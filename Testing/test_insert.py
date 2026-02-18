from Pipelines.ingest import ingest
from Pipelines.evaluate import evaluate
from Pipelines.insert import insert

# Chess.com username and time frame
USERNAME = 'bkchessmaster2'
START_DATE = '2026-01'
END_DATE = '2020-02'

# Ingestion
meta_df, move_df = ingest(USERNAME, START_DATE, END_DATE)

# Evaluation
eval_df = evaluate(move_df, depth=8, username=USERNAME)

# Database insertion
insert(meta_df,eval_df,username=USERNAME)