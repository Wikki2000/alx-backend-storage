-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.

-- drop procedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- create procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
    BEGIN
        UPDATE users 
            -- set average score
            SET average_score = (
                -- compute average
                SELECT SUM(score * weight) / SUM(weight) 
                FROM corrections
                -- join with projects
                INNER JOIN projects ON corrections.project_id = projects.id
                WHERE corrections.user_id = users.id
            );
    END;
$$
DELIMITER;