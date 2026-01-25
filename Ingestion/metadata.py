import chess.pgn as ch          # PGN parser from python-chess
import pandas as pd
from pathlib import Path


class MetaData:
    """
    Extract game-level metadata from a PGN file and store as DataFrame.
    """
    def __init__(self, pgn_path: str):
        # Resolve the project root (two levels up from this file)
        self.project_root = Path(__file__).resolve().parents[1]

        # Build the absolute path to the PGN file
        self.pgn_path = self.project_root / Path(pgn_path)

        # Extract all game metadata immediately upon initialization
        self.df = self._extract_metadata()
    
    def _extract_metadata(self) -> pd.DataFrame:
        """Read the PGN file and extract metadata for all games."""
        # Accumulate metadata dictionaries for each game
        metadata_list = []
        
        # Open the PGN file safely, ignoring malformed characters
        with open(self.pgn_path, encoding="utf-8", errors="ignore") as pgn:
            game_id = 1

            # Read games sequentially until EOF
            while True:
                game = ch.read_game(pgn)
                if game is None:
                    break
                
                # Convert PGN headers to a dictionary
                headers = dict(game.headers)

                # Attach a unique game identifier
                headers["game_id"] = game_id
                game_id += 1

                # Store metadata for this game
                metadata_list.append(headers)
        
        # Return empty DataFrame if no games were found
        if not metadata_list:
            return pd.DataFrame()
        
        # Convert metadata list into a DataFrame
        df = pd.DataFrame(metadata_list)

        # Use game_id as the DataFrame index
        df.set_index("game_id", inplace=True)

        return df
    
    def save_csv(self, output_path: str) -> None:
        """Save metadata as CSV to Data/Silver directory."""
        
        # Persist the metadata DataFrame to disk
        self.df.to_csv(output_path, index=True)

        # Confirm save location to the user
        print(f"Saved to {output_path}")