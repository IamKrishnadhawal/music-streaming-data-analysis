-- Let's see your top 10 most played artists
SELECT 
    performer, 
    COUNT(*) as play_count
FROM my_streaming_activity
GROUP BY performer
ORDER BY play_count DESC
LIMIT 10;

SELECT 
    a.performer, 
    COUNT(a.song) AS play_count,
    ROUND(AVG(f.energy), 2) AS avg_energy
FROM my_streaming_activity AS a
JOIN scrobble_features AS f 
    ON a.performer = f.performer 
    AND a.song = f.song
GROUP BY a.performer
ORDER BY play_count DESC
LIMIT 10;