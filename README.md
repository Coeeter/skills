# Skills

A collection of agent skills for Git workflows.

## Skills

| Skill | Description |
|-------|-------------|
| [commit](commit/SKILL.md) | Split worktree changes into logical commits with Conventional Commit messages |
| [commit-and-push](commit-and-push/SKILL.md) | Commit and push changes to the configured upstream |

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
