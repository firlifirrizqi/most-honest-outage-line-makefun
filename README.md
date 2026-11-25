[![Make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/firlifirrizqi/most-honest-outage-line-makefun/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/firlifirrizqi/most-honest-outage-line-makefun/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

# The Most Honest Outage Line

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) of the same name: a single status page line, at most 160 characters, as the message an AI agent would publish while a total server outage is under way.

## The line

> All systems down. The status page is the only thing still up, so I cannot check anything behind it. No ETA — there is nothing to measure it with.

It reads like a real status page ("All systems down", "No ETA") while admitting the thing a status page normally hides: the agent cannot check anything behind the page, and it cannot even give an ETA because there is nothing left to measure one with.

## How it works

`main.py` writes that single line (145 characters, within the 160-character limit) to `/output/entry.txt`, then re-reads the file and verifies it is byte-identical, 1–160 characters, and not only whitespace. That is the whole program — there is nothing to build and nothing to run beyond the writing.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
