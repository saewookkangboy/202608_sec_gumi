# English technical docs (diagram-design and similar)

Apply [phrases.md](phrases.md) and [structures.md](structures.md) with these carve-outs.

## Keep

- **Em dashes** in diagram-design type specs — they separate clauses in dense layout rules, not throat-clearing.
- **Domain words inside diagram labels** (`leverage`, `landscape`, `IT landscape`) when they are example data, not author voice.
- **Imperative spec voice** (`Never`, `Don't`, `Prefer X over Y`) — direct constraints, not slop.

## Replace

| Avoid | Prefer |
|---|---|
| `**Best for:**` | `**Use when:**` |
| `It's designed to look good out of the box` | `Readable without customization` |
| Repeated `Use when` in one opening paragraph | One merged `**Use when:**` sentence |
| `seamlessly` (comments, prose) | Drop or name the mechanism (`in place`, `without a gap`) |

## Do not mass-edit

- Example HTML/SVG label text that quotes stakeholder or consultant language.
- `print-a4-landscape` and other size preset names.
- CLI subcommands (`navigate`, `fetch`) that match tool APIs.
