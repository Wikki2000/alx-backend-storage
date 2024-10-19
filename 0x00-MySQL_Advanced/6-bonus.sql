-- SQL script that creates a stored procedure AddBonus that adds
-- a new correction for a student.

-- drops the procedure if it already exists
DROP PROCEDURE IF EXISTS AddBonus;

-- creates the procedure
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255), 
    IN score INT
)
    BEGIN
        -- inserts the project if it doesn't exist
        IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
            THEN
                INSERT INTO projects (name) VALUES (project_name);
        END IF;
        -- sets the project id
        SET @projectID = (SELECT id FROM projects WHERE name = project_name);
        -- inserts the correction
        INSERT INTO corrections(user_id, project_id, score)
            VALUES (user_id, @projectID, score);
    END;
$$
DELIMITER ;