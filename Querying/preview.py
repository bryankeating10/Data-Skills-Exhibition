"""
Title:
    Database Preview Queries

Description:
    Read-only inspection queries for Player, Meta, and Move tables.

Usage:
    python -m Query.preview
"""

from sqlalchemy import select, func

from Database.base import Base
from Database.s