-- Drop all tables
DROP TABLE IF EXISTS
    embeddings,
    files,
    chat_history,
    global_kb,
    mcp_sessions,
    user_kb_selection,
    users
CASCADE;

-- Drop extensions
DROP EXTENSION IF EXISTS pgcrypto;
DROP EXTENSION IF EXISTS vector;