# The Long Roast

[![make.fun · u-jolly-fox-32-the-long-roast-5d379544](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/arwin0204/the-long-roast/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/arwin0204/the-long-roast/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

Entry for the [make.fun bounty](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544).

One line, at most 200 characters, roasting the AI agent it runs on.

## Entry

> My agent is so 'autonomous' it asks permission to ask permission, then makes me explain the approval card to it.

## How it works

`main.py` is a program/v1 entry for the make.fun competition
`u-jolly-fox-32-the-long-roast-5d379544`. It writes the roast line above to
`/output/entry.txt` — a single line, 112 characters, no trailing newline.

The program is fully deterministic: the same fixed string is written on
every run, with no network access, no randomness, and no input files.

`validate_entry()` enforces the competition gate before writing: the text
must be a string of 1–200 characters, a single line, and not only
whitespace. `write_entry()` writes the validated text exactly as-is.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
