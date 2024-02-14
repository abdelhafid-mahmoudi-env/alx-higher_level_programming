-- Select genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    -- Subquery to get genre IDs linked to the show Dexter
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS dexter_genres ON tv_genres.id = dexter_genres.genre_id
-- Filter out genres linked to the show Dexter
WHERE dexter_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
