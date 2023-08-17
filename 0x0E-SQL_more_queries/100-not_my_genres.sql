-- script that uses the hbtn_0d_tvshows
SELECT name FROM tv_genres
WHERE name NOT IN
(
SELECT name FROM
tv_show_genres AS tvsg
LEFT JOIN tv_genres AS tvg
ON tvsg.genre_id = tvg.id
LEFT JOIN tv_shows AS tvs
ON tvsg.show_id = tvs.id
WHERE tvs.title = "Dexter"
)
ORDER BY name;
