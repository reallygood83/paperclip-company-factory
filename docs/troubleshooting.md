# Troubleshooting

## Paperclip health check fails
- Make sure `npx paperclipai run` is running
- Check `PAPERCLIP_BASE_URL` and `PAPERCLIP_API_PREFIX`

## Hermes integration feels incomplete
- Start with manual natural-language to structured-action mapping
- Keep dangerous actions behind approval

## Company creation endpoint differs
- Some Paperclip versions may expose different create-company endpoints
- Use `create-company --dry-run` first and inspect the generated payload
