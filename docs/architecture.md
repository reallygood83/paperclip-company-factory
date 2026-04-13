# Architecture

paperclip-company-factory has four layers:

1. Hermes as natural-language orchestrator
2. Factory CLI + templates as reproducible company bootstrap layer
3. Paperclip as runtime for companies, agents, issues, and activity
4. Optional self-host deployment layer (Docker Compose / VPS / Coolify)

The public OSS design goal is reproducibility rather than tight coupling to one developer machine.
