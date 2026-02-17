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
from Processing.add_eval import add_eval, repop
from Processing.unique_fen import unique_fens

def evaluate(move_df, username: str, depth=20):
    # Extract unique FENs into a Series to avoid redundant evaluations
    unique = unique_fens(move_df)

    # Evaluate unique FENs using Stockfish at desired depth
    evaluated_fens = add_eval(unique, depth=depth)

    # Map evaluations back to the moves df
    eval_df = repop(move_df, evaluated_fens)

    # Save as backup
    eval_df.to_csv(f'Data/Gold/{username}_move.csv')

    return eval_df

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        evaluate(sys.argv[1])
        print("\nEvaluation for {username} complete.\n")
    else:
        print("Usage: python -m evaluate <move_df> \nor \n" \
        "evaluate(move_df, depth=25, username=<username>)")