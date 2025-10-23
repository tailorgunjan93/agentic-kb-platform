-- Dummy user
INSERT INTO users (email, password_hash, role)
VALUES ('demo@agentic.ai', 'hashed_dummy_password', 'user');

-- Insert uploaded file
INSERT INTO files (user_id, filename, file_type, visibility, path)
VALUES (
    (SELECT id FROM users WHERE email = 'demo@agentic.ai'),
    'human-nutrition-text.pdf',
    'pdf',
    'public',
    'backend/uploads/human-nutrition-text.pdf'
);

-- Insert dummy embeddings (3 chunks)
INSERT INTO embeddings (file_id, chunk_index, content, embedding)
VALUES
(
    (SELECT id FROM files WHERE filename = 'human-nutrition-text.pdf'),
    0,
    'Nutrition is the biochemical and physiological process by which an organism uses food.',
    ('[' || array_to_string(ARRAY(SELECT generate_series(1, 384) * 0.001), ',') || ']')::vector
),
(
    (SELECT id FROM files WHERE filename = 'human-nutrition-text.pdf'),
    1,
    'It includes ingestion, absorption, assimilation, biosynthesis, catabolism, and excretion.',
    ('[' || array_to_string(ARRAY(SELECT generate_series(1, 384) * 0.001), ',') || ']')::vector
),
(
    (SELECT id FROM files WHERE filename = 'human-nutrition-text.pdf'),
    2,
    'The science of nutrition attempts to understand how and why specific dietary aspects influence health.',
    ('[' || array_to_string(ARRAY(SELECT generate_series(1, 384) * 0.001), ',') || ']')::vector
);

-- Optional: Add to global_kb
INSERT INTO global_kb (title, category, content, source_type, kb_group)
VALUES (
    'Human Nutrition Overview',
    'Healthcare',
    'This document covers the fundamentals of human nutrition including digestion, absorption, and dietary impact.',
    'file',
    'nutrition'
);