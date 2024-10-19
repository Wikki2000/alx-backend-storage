-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.

-- removes the trigger if it already exists
DROP TRIGGER IF EXISTS validate_email;

-- creates the trigger
DELIMITER $$
CREATE TRIGGER reset_valid_email_attr
    BEFORE UPDATE ON users
        FOR EACH ROW
        BEGIN
            IF OLD.email <> NEW.email THEN
                SET NEW.valid_email = 0;
            END IF;
         END;
$$
DELIMITER ;