-- SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store the
-- average score for a student

-- Drop procedure if already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
    BEGIN
        UPDATE users
        -- set average score
        SET average_score = (
            SELECT AVG(score) FROM corrections
            WHERE corrections.user_id = user_id
        )
        WHERE id = user_id;
    END;
$$
DELIMITER ;