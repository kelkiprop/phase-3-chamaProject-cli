from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic import context
import os

# Load the Alembic configuration
config = context.config

# Manually set the database URL (this is important)
config.set_main_option("sqlalchemy.url", "sqlite:///chama.db")

# Set up logging
fileConfig(config.config_file_name)

# Import your models
from database import Base  # Ensure Base is imported correctly

# Set target metadata
target_metadata = Base.metadata

# Run migrations
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
