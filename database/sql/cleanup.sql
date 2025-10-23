-- Cleanup all data from tables
TRUNCATE
    embeddings,
    files,
    chat_history,
    global_kb,
    mcp_sessions,
    user_kb_selection,
    users
RESTART IDENTITY CASCADE;