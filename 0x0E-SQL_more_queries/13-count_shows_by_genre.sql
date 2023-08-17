-- script that lists all shows contained in hbtn_0d_tvshows

SELECT tvg.name AS genre, COUNT(tvg.name) AS number_of_shows
FROM tv_show_genres AS tvsg
JOIN tv_shows AS tvs
ON tvsg.show_id=tvs.id
JOIN tv_genres AS tvg
ON tvsg.genre_id=tvg.id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
