#!/bin/bash

# SMK NEGERI 1 TANJUNG LAGO - Auto Update Script
# Skrip ini akan menarik perubahan terbaru dari GitHub dan merestart sistem

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}====================================================${NC}"
echo -e "${GREEN}   SMK NEGERI 1 TANJUNG LAGO - AUTO UPDATER${NC}"
echo -e "${BLUE}====================================================${NC}"

# Cek apakah dijalankan sebagai root
if [ "$EUID" -ne 0 ]; then 
  echo "Harap jalankan sebagai root (sudo bash update.sh)"
  exit
fi

echo -e "${BLUE}Menarik perubahan terbaru dari GitHub...${NC}"
git pull origin main

echo -e "${BLUE}Mengatur izin eksekusi script...${NC}"
chmod +x docker-entrypoint.sh
chmod +x deploy.sh
chmod +x update.sh

echo -e "${BLUE}Membangun ulang dan merestart container...${NC}"
docker-compose up -d --build
docker-compose -f docker-compose.challenges.yml up -d --build

# Bersihkan image docker yang tidak terpakai
docker image prune -f

echo -e "${GREEN}Sistem berhasil diupdate dan dijalankan ulang!${NC}"
echo -e "Cek website Anda sekarang."
