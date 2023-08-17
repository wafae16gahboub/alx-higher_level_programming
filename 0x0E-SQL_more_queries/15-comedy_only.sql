-- lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tvs.title
FROM tv_show_genres AS tvsg
JOIN tv_shows AS tvs
ON tvsg.show_id=tvs.id
JOIN tv_genres AS tvg
ON tvsg.genre_id=tvg.id
WHERE tvg.name="Comedy"
ORDER BY tvs.title;
