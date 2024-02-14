-- Select genre name from tv_genres table
-- Join tv_shows, tv_show_genres, and tv_genres tables
-- Filter records where the title is "Dexter"
-- Sort the results in ascending order by the genre name
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
