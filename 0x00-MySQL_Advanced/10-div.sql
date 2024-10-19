--  SQL script that creates a function SafeDiv that divides
--  (divides) the first by the second number and returns
--  0 if the second number is equal to 0.

-- drop function if exists
DROP FUNCTION IF EXISTS SafeDiv;

-- creates function
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
    BEGIN
        IF b = 0 THEN
            RETURN 0;
        ELSE
            RETURN (a / b);
        END IF;
    END;
$$
DELIMITER ;