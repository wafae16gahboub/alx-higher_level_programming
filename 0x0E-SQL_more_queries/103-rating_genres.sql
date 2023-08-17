-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_show_genres AS tsg
JOIN tv_show_ratings AS tsr
ON tsr.show_id = tsg.show_id
JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY rating DESC;
