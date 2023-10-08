---
layout: post
title: "[Tool] HomeBrew"
date: 2019-03-14 00:00 +0000
---
HomeBrew is a good tool and fill the final piece of the puzzle for me to switch from Linux to Mac.

## Installation

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Usage

```bash
brew install <package>
brew uninstall <package>
brew list
brew search <package>
brew info <package>
brew update
brew upgrade
brew outdated
brew cleanup
brew doctor
```

## Services

```bash
brew services list
brew services start <service>
brew services stop <service>
brew services restart <service>
brew services cleanup
```

## Mirror

You can use a mirror to speed up the download, such as [Aliyun](https://developer.aliyun.com/mirror/homebrew?spm=a2c6h.13651102.0.0.3e221b11x81HJE).

```bash
# replace homebrew
cd "$(brew --repo)"
git remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git

brew update

# replace homebrew-bottles
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles' >> ~/.zshrc
```


# Reference

