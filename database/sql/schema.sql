-- ✅ Enable required extensions
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "vector";

-- 👤 Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 📁 Files table
CREATE TABLE files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    filename TEXT NOT NULL,
    file_type TEXT,
    visibility TEXT DEFAULT 'private',
    path TEXT NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🧠 Embeddings table
CREATE TABLE embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    file_id UUID REFERENCES files(id),
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(384) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 💬 Chat history table
CREATE TABLE chat_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    message TEXT NOT NULL,
    response TEXT,
    agent_used TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🌐 Global knowledge base
CREATE TABLE global_kb (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    category TEXT,
    content TEXT NOT NULL,
    source_url TEXT,
    source_type TEXT DEFAULT 'manual',
    kb_group TEXT,
    visibility TEXT DEFAULT 'public',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 📌 User KB selection
CREATE TABLE user_kb_selection (
    user_id UUID REFERENCES users(id),
    kb_group TEXT NOT NULL,
    selected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, kb_group)
);

-- 🧾 Optional: Multi-agent session logs
CREATE TABLE mcp_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    session_id TEXT,
    agent_name TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🔍 Index for semantic search
CREATE INDEX idx_embeddings_vector ON embeddings USING ivfflat (embedding vector_cosine_ops);