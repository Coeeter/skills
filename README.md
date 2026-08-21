# Skills

A collection of personal agent workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [commit](commit/SKILL.md) | Propose and create an approved batch of Conventional Commits |
| [commit-and-push](commit-and-push/SKILL.md) | Commit and push changes to the configured upstream |
| [execute-approved-plan](execute-approved-plan/SKILL.md) | Deliver the smallest complete implementation of an agreed plan |

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
