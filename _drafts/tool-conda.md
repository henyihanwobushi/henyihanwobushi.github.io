---
layout: post
title: "[tool] Conda"
---

Conda is a package manager for Python. It is a tool for installing packages from the Python Package Index (PyPI) as well as other indexes. Conda is also an environment manager application. A conda environment is a directory that contains a specific collection of conda packages that you have installed. For example, you may have one environment with NumPy 1.7 and its dependencies, and another environment with NumPy 1.6 for legacy testing. If you change one environment, your other environments are not affected. You can easily activate or deactivate environments, which is how you switch between them. You can also share your environment with someone by giving them a copy of your environment.yaml file.

## Command Cheat Sheet

| Action                    | Command                           | Description                                  |
| ------------------------- | --------------------------------- | -------------------------------------------- |
| Create a new environment  | `conda create --name myenv`       | Create a new environment with the name myenv |
| Activate an environment   | `conda activate myenv`            | Activate the environment myenv               |
| Deactivate an environment | `conda deactivate`                | Deactivate the current environment           |
| Remove an environment     | `conda remove --name myenv --all` | Remove the environment myenv                 |