-- script that lists all shows contained in hbtn_0d_tvshows(imported dump file)
-- display: tv_shows.title - tv_show_genres.genre_id,Results sorted in asc order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
