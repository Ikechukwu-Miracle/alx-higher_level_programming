-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tvshow_ratings.rating) AS rating_sum
FROM tv_genres
LEFT JOIN tvshow_genres ON tv_genres.id = tvshow_genres.genre_id
LEFT JOIN tv_shows ON tvshow_genres.show_id = tv_shows.id
LEFT JOIN tvshow_ratings ON tv_shows.id = tvshow_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
