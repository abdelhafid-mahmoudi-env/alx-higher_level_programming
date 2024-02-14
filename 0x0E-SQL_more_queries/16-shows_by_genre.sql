-- Select the show title and genre name from the tv_shows and tv_genres tables
-- Left join the tv_show_genres table to include all shows even if they don't have linked genres
-- Sort the results in ascending order by the show title and genre name
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
