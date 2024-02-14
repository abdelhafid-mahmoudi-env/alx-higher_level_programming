USE hbtn_0c_0;

-- Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field 'name' to UTF8
ALTER TABLE first_table MODIFY COLUMN `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
