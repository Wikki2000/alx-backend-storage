-- SQL script that creates a view need_meeting that lists
-- all students that have a score under 80 (strict) and 
-- have no last_meeting or more than 1 month.

-- drops view if it exists
DROP VIEW IF EXISTS need_meeting;

-- creates view
CREATE VIEW need_meeting AS
    SELECT name
    FROM students
    WHERE score < 80
    AND (last_meeting IS NULL
    OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH))