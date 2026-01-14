#!/usr/bin/env bash

echo "Codespaces keep-alive started..."

while true; do
  # simuliraj mali stdout koji Codespaces registrira
  echo "keepalive $(date)"
  sleep 60
done
