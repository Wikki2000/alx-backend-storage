-- SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes and store
-- the average weighted score for a student.

-- drop procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- create procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
    BEGIN
        -- update average score
        UPDATE users
            SET average_score = (
                -- get sum of scores
                SELECT SUM(score * weight) / SUM(weight)
                FROM corrections
                -- join with projects
                INNER JOIN projects ON corrections.project_id = projects.id
                WHERE corrections.user_id = user_id
            )
        WHERE id = user_id;
    END; 
$$
DELIMITER ;