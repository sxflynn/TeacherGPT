-- Displays all tables that do not contain any foreign keys

SELECT nspname AS schema_name, relname AS table_name
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE c.relkind = 'r' -- regular table
  AND NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conrelid = c.oid AND contype = 'f'
    )
  AND nspname NOT IN ('pg_catalog', 'information_schema') -- exclude system tables
ORDER BY schema_name, table_name;