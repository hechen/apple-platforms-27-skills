# Installation and agent compatibility

Install the **complete set of nine skill directories**. Shared platform/framework guidance uses sibling relative links. Copying only `SKILL.md` loses supporting references; installing only the coordinator leaves its routes unresolved.

## Option A: Skills CLI

From your application repository:

```sh
npx skills add hechen/apple-platforms-27-skills --skill '*'
```

Choose one or more agents interactively. To select a host explicitly, replace `claude-code` below with an ID from the table:

```sh
npx skills add hechen/apple-platforms-27-skills --skill '*' --agent claude-code
```

| Agent | CLI ID |
|---|---|
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |
| Gemini CLI | `gemini-cli` |
| Windsurf / Cascade | `windsurf` |
| OpenCode | `opencode` |
| Cline | `cline` |
| Roo Code | `roo` |
| Continue | `continue` |
| Antigravity | `antigravity` |
| Amp | `amp` |
| OpenClaw | `openclaw` |
| Codex | `codex` |

Multiple IDs can follow `--agent`. Add `--global` for user-wide installation, `--copy` when symlinks are unsuitable, and `--yes` only when you want noninteractive installation. Use `--skill '*'` to select this full collection; `--all` also selects every supported agent and is broader than most installations need. See the [upstream Skills CLI](https://github.com/vercel-labs/skills) for its current agent list and options.

## Option B: GitHub CLI

If your GitHub CLI includes `gh skill`, it can install the same repository:

```sh
gh skill install hechen/apple-platforms-27-skills --all --agent claude-code
gh skill install hechen/apple-platforms-27-skills --all --agent github-copilot
```

Run one command for the agent you use. Add `--scope user` for a user-wide install. Check `gh skill install --help` for supported IDs; its agent catalog can differ from the Skills CLI. Use `--pin <tag-or-commit>` for a reproducible version. Do not use `--force` to overwrite locally edited skills unless that is intentional. See the [GitHub CLI manual](https://cli.github.com/manual/gh_skill_install).

## Option C: Manual installation

Clone or download the repository, then copy the nine directories inside `skills/` into your agent's supported skill directory. Preserve their names and internal files.

Common **project** locations documented by the hosts include:

| Host | Project skill directory | Source |
|---|---|---|
| Claude Code | `.claude/skills/` | [Claude documentation](https://code.claude.com/docs/en/skills) |
| Cursor | `.cursor/skills/` | [Cursor documentation](https://cursor.com/docs/skills) |
| GitHub Copilot | `.github/skills/` | [GitHub documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| Gemini CLI | `.gemini/skills/` | [Gemini documentation](https://geminicli.com/docs/cli/skills/) |
| Windsurf / Cascade | `.windsurf/skills/` | [Cascade documentation](https://docs.windsurf.com/windsurf/cascade/skills) |
| OpenCode | `.opencode/skills/` | [OpenCode documentation](https://opencode.ai/v2/docs/skills) |

Many current hosts also accept `.agents/skills/`. Installer-selected paths may use that shared location rather than the host-specific path above. Follow the current host documentation and avoid installing duplicate copies of a skill into several paths scanned by the same host.

For other hosts, use the installer catalog or the agent’s documented custom skill directory. A folder name alone cannot make an older agent version support skills.

## Activate and verify

1. Reload the host's skill catalog or start a new session if required.
2. Confirm `apple-platforms-27` is visible using that host's skill list/picker, when available.
3. Ask the agent to use it on a bounded task, such as identifying affected targets and locating the relevant Apple documentation.
4. Check that it can open a linked reference and a sibling skill. Installation must include supporting files, not only the entrypoints.

Explicit invocation differs by host: Claude Code documents slash commands, Cascade documents `@` mentions, and other hosts use a picker or a skill-loading tool. These skills do not require a particular invocation syntax internally.

## Agents without native skills

Give the agent the path to one entrypoint and ask it to read that file and the relevant references before working. Keep the clone accessible. This supports use as ordinary instructions but does not create native discovery, slash commands, or tool permissions.

## Updating

Use the same installer and scope used originally. Review upstream changes before replacing local edits. For teams, pin a release/commit with GitHub CLI or vendor a reviewed snapshot into the app repository. Do not change application deployment targets merely to install updated instructions.
