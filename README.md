# Skills

Shared agent skills, maintained independently of [dotfiles](https://github.com/taekwondodev/dotfiles).

## Install

```sh
git clone git@github.com:taekwondodev/skills.git ~/Developer/skills
mkdir -p ~/.agents
# Requires ~/.agents/skills to be absent; do not overwrite an existing directory.
ln -s ~/Developer/skills/skills ~/.agents/skills
```

Skill directories live under `skills/`. The `~/.agents/skills` symlink points directly to that directory; this repository does not require GNU Stow.

Configure Hermes with:

```yaml
skills:
  external_dirs:
    - ~/.agents/skills
```

Each Hermes profile automatically loads its own local skills in addition to this shared directory. Do not add the default profile's `~/.hermes/skills` to other profiles if they should remain isolated. Profile-local skills, runtime state, and credentials do not belong in this repository.

Existing shared skills may be updated in place by Hermes. Newly created skills stay in the active profile unless its creation directory is explicitly configured otherwise. Start a new Hermes session after changing skill configuration.

## Checks

Run from this repository's root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/eval/tests -v
python3 skills/eval/scripts/validate_dev_cycle.py --baseline-ref HEAD
```

See `skills/eval/SKILL.md` for optional behavioral evaluations, which require a configured Hermes runtime and make model calls. Use `--baseline-ref <commit>` to compare against an explicit commit in this repository. The default is `HEAD`; old dotfiles commit IDs are not baselines in this independent history.

## Origin

The initial import contains the shared skills extracted from dotfiles, with evaluation paths adapted to this repository. Dotfiles history remains in its original repository; unrelated configuration and profile-local skill history are not imported here.
