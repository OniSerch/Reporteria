class config:
    # Database configuration
    SECRET_KEY="your_secret_key_here"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reporteria.db'  # SQLite database file
    sqlalchemy_track_modifications = False  # Disable track modifications to save memory
    JWT_SECRET_KEY  = 'your_jwt'
    DB_HOST = 'localhost'
    DB_PORT = 5432