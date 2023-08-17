-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_show_ratings AS tsr
JOIN tv_shows AS ts
	ON tsr.show_id = ts.id
GROUP BY ts.title
ORDER BY rating DESC;
