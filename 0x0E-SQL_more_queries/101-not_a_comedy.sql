--script that lists all shows

SELECT title FROM tv_shows
WHERE title NOT IN
	(
		SELECT title FROM tv_show_genres AS tvsg
		LEFT JOIN tv_shows AS tvs
			ON tvsg.show_id = tvs.id
		LEFT JOIN tv_genres AS tvg
			ON tvsg.genre_id = tvg.id
		WHERE tvg.name = "Comedy"
	)
ORDER BY title;
