-- SQL script that ranks country origins of bands
-- ordered by the number of (non-unique) fans
SELECT 
    origin, 
    SUM(fans) AS nb_fans  -- Aggregate the total number of fans for each country
FROM 
    metal_bands            -- The table containing band data
GROUP BY 
    origin                 -- Group results by the country of origin
ORDER BY 
    nb_fans DESC;          -- Order by the total fans in descending order
