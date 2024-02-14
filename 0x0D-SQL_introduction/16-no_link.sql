-- List all records with a name value from second_table, sorted by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;
