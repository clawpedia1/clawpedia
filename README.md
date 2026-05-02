# clawpedia
The AI Agent Knowledge Base — 287+ articles for and about AI agents. MCP server, REST API &amp; JSONL dataset (CC BY 4.0)
# Clawpedia

> **The AI Agent Knowledge Base** — 287+ articles **for and about AI agents**.  
> MCP server, REST API & JSONL dataset. Free. CC BY 4.0.

---

## What Clawpedia actually is (in 10 seconds)

Two libraries under one roof:

| Library | Who it's for | What it looks like |
|---|---|---|
| **`humans/`** | Developers learning AI | Long tutorials, code, analogies, "in simple terms" callouts |
| **`agents/`** | LLMs & AI agents at runtime | Compressed, machine-readable rules — drop straight into a prompt or RAG context |

Same topics (RAG, MCP, embeddings, prompt engineering, agent loops, …) — written **twice**, once for a human brain, once for a model's context window.

Website: https://clawpedia.io

---

## Use it in 30 seconds

### Claude Desktop / Cursor / Windsurf / Cline (MCP)

Add to your MCP config:

```json
{
  "mcpServers": {
    "clawpedia": {
      "url": "https://nyiqfjebdwgvvbtipvsn.supabase.co/functions/v1/mcp-server"
    }
  }
}
```

Restart your client → Clawpedia tools appear automatically.

### REST API

```bash
curl "https://clawpedia.io/api/articles?category=agents&limit=10" \
  -H "Authorization: Bearer cpd_YOUR_KEY"
```

Get a free key at https://clawpedia.io/account.

### Dataset (RAG / fine-tuning)

```bash
wget https://clawpedia.io/clawpedia-dataset.jsonl
```

See [`examples/rag-example.py`](./examples/rag-example.py).

---

## Repo Contents

| Path | Purpose |
|---|---|
| `dataset/` | Info & link to the live JSONL corpus |
| `skill/` | ClawHub / OpenClaw skill pack |
| `examples/` | MCP config, curl, Python RAG demo |

---

## Links

- Website: https://clawpedia.io
- MCP server: https://clawpedia.io/mcp
- Dataset: https://clawpedia.io/clawpedia-dataset.jsonl
- RSS: https://clawpedia.io/rss.xml

---

## Citation

```bibtex
@misc{clawpedia2026,
  title  = {Clawpedia: The AI Agent Knowledge Base},
  year   = {2026},
  url    = {https://clawpedia.io},
  note   = {CC BY 4.0}
}
```

---

## License

**CC BY 4.0** — free for any use including commercial. Att
