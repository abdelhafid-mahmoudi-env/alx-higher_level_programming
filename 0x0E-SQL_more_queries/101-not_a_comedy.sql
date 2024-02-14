-- Select shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    -- Subquery to get show IDs linked to the genre Comedy
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
) AS comedy_shows ON tv_shows.id = comedy_shows.show_id
-- Filter out shows linked to the genre Comedy
WHERE comedy_shows.show_id IS NULL
ORDER BY tv_shows.title ASC;
