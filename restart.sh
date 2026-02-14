#!/usr/bin/bash

# 1. 彻底杀掉后台服务和所有残留的 openclaw 进程
systemctl --user stop openclaw-gateway
killall -9 openclaw

# 2. 清除所有历史记忆（非常重要！）
rm -rf ~/.openclaw/agents/main/sessions/*
rm -rf ~/.openclaw/agents/main/queue/*

# 3. start
systemctl --user start openclaw-gateway
