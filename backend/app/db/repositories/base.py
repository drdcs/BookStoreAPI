from databases import Database



class BaseRepository:
    """Our BaseRepository will be a simple class needed only to keep a reference to our database connection. """
    def __init__(self, db: Database) -> None:
        self.db = db