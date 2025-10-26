-- Check files table
SELECT COUNT(*) as file_count FROM files;
SELECT * FROM files LIMIT 5;

-- Check embeddings table
SELECT COUNT(*) as embedding_count FROM embeddings;
SELECT file_id, chunk_index, LEFT(content, 100) as content_preview FROM embeddings LIMIT 5;
