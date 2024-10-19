-- SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order.

-- removes the prev triger if exists
DROP TRIGGER IF EXISTS reduce_quantity;

-- creates the triger
CREATE TRIGGER decrease_q 
    AFTER INSERT ON orders 
    FOR EACH ROW
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
