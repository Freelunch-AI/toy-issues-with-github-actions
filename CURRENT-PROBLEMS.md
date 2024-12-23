# CURRENT PROBLEMS  

Why use this file instead of Github Issues? Because the issues in this project are already being used for the app (LLMOps issue resolver).

## Problem 1

### Description

▶ Run uv venv
Using CPython 3.12.8 interpreter at: /opt/hostedtoolcache/Python/3.12.8/x64/bin/python3
Creating virtual environment at: .venv
  × Failed to download `llmops-issue-resolver @
  │ https://github.com/BrunoScaglione/llmops-issue-resolver/blob/main/llmops-issue-resolver/dist/llmops_issue_resolver-0.1.0-py3-none-any.whl`
  ├─▶ Failed to read metadata:
  │   `https://github.com/BrunoScaglione/llmops-issue-resolver/blob/main/llmops-issue-resolver/dist/llmops_issue_resolver-0.1.0-py3-none-any.whl`
  ├─▶ Failed to read from zip file
  ╰─▶ Encountered an unexpected header (actual: 0xa0a0a0a, expected:
      0x4034b50).
Error: Process completed with exit code 1.

### Comments

This problem is weird because I used uv to build the .whl and I even tested installing it locally (Windows machine) and it worked.

Already tried putting everything on python 3.9, and the problem remains.

I'm suspecting it has to do with Windows/Linux. Because it install lcally on Windows, but doesnt install remotely on Linux (both are using python 3.9).