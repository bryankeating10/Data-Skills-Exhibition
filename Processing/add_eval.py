import pandas as pd
from stockfish import Stockfish
import chess

# Stockfish path
STOCK_PATH = r"C:\Tools\stockfish\stockfish-windows-x86-64-avx2.exe"

# Check if FEN is valid and represents a legal position (including Chess960).
def is_valid_fen(fen: str) -> bool:
    try:
        # Try standard chess first
        board = chess.Board(fen)
        if board.is_valid():
            return True
    except:
        pass
    
    try:
        # If standard fails, try Chess960
        board = chess.Board(fen, chess960=True)
        return board.is_valid()
    except:
        return False

# Add Stockfish evaluation to a unique FEN Series.
def add_eval(unique_fen_series: pd.Series, depth: int = 15) -> pd.Series:

    # Initialize Stockfish and accept Chess960 positions
    stockfish = Stockfish(path=STOCK_PATH, depth=depth)
    stockfish.update_engine_parameters({"UCI_Chess960": True})
    
    total = len(unique_fen_series)
    invalid_count = 0
    evaluated_count = 0
    
    print(f"Evaluating {total} unique positions at depth {depth}...")
    
    # Iterate through the index (FEN strings)
    for i, fen in enumerate(unique_fen_series.index):
        
        # Validate FEN first
        if not is_valid_fen(fen):
            print(f"Invalid FEN at position {i}: {fen[:50]}...")
            unique_fen_series.iloc[i] = None  # Or 0.0
            invalid_count += 1
            continue
        
        try:
            stockfish.set_fen_position(fen)
            evaluation = stockfish.get_evaluation()
            
            # Extract value
            if evaluation['type'] == 'cp':
                eval_value = evaluation['value'] / 100.0  # Convert centipawns
            else:  # mate
                eval_value = f"M{evaluation['value']}"
            
            unique_fen_series.iloc[i] = eval_value
            evaluated_count += 1
        
        # Handle errors to ensure game_id coherence with original DataFrame
        except Exception as e:
            print(f"Error at position {i}: {e}")
            unique_fen_series.iloc[i] = None
        
        # Progress
        if (i + 1) % 50 == 0:
            print(f"Evaluated {i + 1}/{total} positions... ({invalid_count} invalid)")
    
    print(f"\nCompleted: {total} positions")
    print(f"Successfully evaluated: {evaluated_count}")
    print(f"Invalid FENs: {invalid_count}")
    
    return unique_fen_series

# Map evaluations from unique FEN series back to the original moves dataframe.
def repopulate_unique_evals(moves_df, unique_fen_series):
    moves_df['eval'] = moves_df['fen'].map(unique_fen_series)
    return moves_df