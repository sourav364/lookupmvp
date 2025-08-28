# lookup

Minimal MVP for the lookup project.

## Quickstart

```bash
make install
cp .env.example .env  # set your variables
make api   # start FastAPI server
make app   # start Streamlit app
make worker  # start background worker
```

### Docker

```bash
make up
```

## Architecture

```
+-------------+      +-----------+
| Streamlit   | ---> |  FastAPI  |
+-------------+      +-----------+
        \                |
         \               v
          \          +--------+
           \-------->|  RQ    |
                     +--------+
```

## Next Milestones
- Implement real planning and tools
- Persist jobs and dashboards in DuckDB
- Add authentication and user management

