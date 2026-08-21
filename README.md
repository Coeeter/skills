# Skills

A collection of personal agent workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [commit](commit/SKILL.md) | Propose and create an approved batch of Conventional Commits |
| [commit-and-push](commit-and-push/SKILL.md) | Commit and push changes to the configured upstream |
| [create-plan](create-plan/SKILL.md) | Grill and turn a feature into an approved implementation plan |
| [execute-approved-plan](execute-approved-plan/SKILL.md) | Execute an approved plan continuously with local phase commits |
| [init-agent](init-agent/SKILL.md) | Initialize repository instructions, context, and project skills |
| [inline-advisor](inline-advisor/SKILL.md) | Consult another local coding model as a read-only advisor |

## Installation

Install with the [Vercel Skills CLI](https://skills.sh):

```bash
npx skills add Coeeter/skills
```

This symlinks the skills into your agent's skill directories. Use `-g` to install globally instead of per-project.

### Options

| Flag | Description |
|------|-------------|
| `-g` | Install to `~/<agent>/skills/` instead of `./<agent>/skills/` |
| `-a <agent>` | Target a specific agent (e.g., `claude-code`, `opencode`) |
| `-s <skill>` | Install only specific skills by name |
| `-y` | Skip confirmation prompts |
