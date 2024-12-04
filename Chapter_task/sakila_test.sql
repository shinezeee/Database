use sakila;

-- 1. 배우 'GUINESS PENELOPE'가 출연한 모든 영화 제목 조회
SELECT movie.title
FROM film movie
JOIN film_actor fa on movie.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = "PENELOPE" and a.last_name = "GUINESS"

-- 