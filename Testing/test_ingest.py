from Pipelines.ingest import ingest

meta_df, move_df = ingest('bkchessmaster2','2026-01','2026-02')

print('METADATA')
print(meta_df.head(7))

print('MOVEDATA')
print(move_df.head(7))