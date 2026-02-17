"""
Title:
    Docstring for Pipelines.evaluate

Description:
    Function for evaluation of move data, backing up the 
    results in /Data

Usage:
    evaluate(move_df)
        or
    evaluate(move_df, depth==25)

Output:
    Dataframe containing evaluated positions
"""

# Evaluation modules
from Processing.add_eval import add_eval, repopulate_unique_evals
from Processing.unique_fen import unique_fens

