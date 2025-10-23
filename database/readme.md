# 📦 Semantic Agent-Based Knowledge Platform – Database Layer

This PostgreSQL schema powers a modular agentic knowledge base system with support for file ingestion, semantic search, multi-agent workflows, and curated global knowledge. It uses `pgvector` for embeddings and `pgcrypto` for UUID generation.

---

## 🧱 Schema Overview

| Table              | Purpose                                      |
|--------------------|----------------------------------------------|
| `users`            | Stores user credentials and roles            |
| `files`            | Tracks uploaded documents                    |
| `embeddings`       | Stores chunked text and vector embeddings    |
| `chat_history`     | Logs user-agent interactions                 |
| `global_kb`        | Curated knowledge entries (manual, file, URL)|
| `user_kb_selection`| Tracks user-selected KB groups               |
| `mcp_sessions`     | Optional logs for multi-agent workflows      |

---

## 🧠 Extensions

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto"; -- UUID generation
CREATE EXTENSION IF NOT EXISTS "vector";   -- pgvector for semantic search