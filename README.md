# Skills

A collection of personal agent workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [commit](commit/SKILL.md) | Propose and create an approved batch of Conventional Commits |
| [commit-and-push](commit-and-push/SKILL.md) | Commit and push changes to the configured upstream |
| [create-spec](create-spec/SKILL.md) | Define and stress-test a feature before implementation |
| [create-plan](create-plan/SKILL.md) | Turn an approved feature spec into an implementation plan |
| [execute-approved-plan](execute-approved-plan/SKILL.md) | Execute an approved plan as a live implementation ledger |

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
