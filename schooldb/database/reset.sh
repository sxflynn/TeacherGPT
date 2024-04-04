#!/bin/bash

# Directory containing your SQL files
SQL_DIR=/docker-entrypoint-initdb.d

# Loop through each SQL file in the directory and execute it
for sql_file in $SQL_DIR/*.sql; do
    echo "Executing $sql_file..."
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f $sql_file
done
