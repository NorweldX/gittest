#!/bin/bash


DATE=$(date +%Y-%m-%d_%H-%M)
BACKUP_DIR="$HOME/backups"

if [ ! -d "$BACKUP_DIR"  then
    mkdir -p "$BACKUP_DIR"
fi

tar -czf "$BACKUP_DIR/ssh_backup_$DATE.tar.gz" /etc/ssh



echo "=== Запуск скрипта: $DATE ==="




df -h
