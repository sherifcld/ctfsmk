#!/bin/bash

# SMK NEGERI 1 TANJUNG LAGO - Auto Deploy Script
# Skrip ini mengotomatisasi instalasi Docker, Nginx, dan SSL Certbot

# Warna untuk output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}====================================================${NC}"
echo -e "${GREEN}   SMK NEGERI 1 TANJUNG LAGO - CTF DEPLOYER${NC}"
echo -e "${BLUE}====================================================${NC}"

# Cek apakah dijalankan sebagai root
if [ "$EUID" -ne 0 ]; then 
  echo "Harap jalankan sebagai root (sudo bash deploy.sh)"
  exit
fi

# Input Domain
read -p "Masukkan Domain Anda (contoh: ctf.smkn1tanjunglago.sch.id): " DOMAIN
if [ -z "$DOMAIN" ]; then
    echo "Domain tidak boleh kosong!"
    exit 1
fi

read -p "Masukkan Email untuk SSL Certbot: " EMAIL
if [ -z "$EMAIL" ]; then
    echo "Email tidak boleh kosong!"
    exit 1
fi

echo -e "\n${BLUE}[1/5] Menginstal Dependensi Sistem...${NC}"
apt-get update
apt-get install -y curl git apt-transport-https ca-certificates software-properties-common certbot python3-certbot-nginx python3-pip

# Fix AttributeError: module 'lib' has no attribute 'X509_V_FLAG_NOTIFY_POLICY'
echo -e "${BLUE}Memperbaiki dependensi OpenSSL/Cryptography...${NC}"
pip3 install --upgrade pyOpenSSL cryptography

# Instal Docker jika belum ada
if ! command -v docker &> /dev/null; then
    echo -e "${BLUE}Menginstal Docker...${NC}"
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    usermod -aG docker $USER
fi

# Instal Docker Compose jika belum ada
if ! command -v docker-compose &> /dev/null; then
    echo -e "${BLUE}Menginstal Docker Compose...${NC}"
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
fi

echo -e "\n${BLUE}[2/5] Mengonfigurasi Nginx...${NC}"
# Buat konfigurasi Nginx sementara untuk tantangan Certbot
cat > ./conf/nginx/http.conf <<EOF
worker_processes 4;
events { worker_connections 1024; }
http {
    upstream app_servers { server ctfd:8000; }
    server {
        listen 80;
        server_name $DOMAIN;
        location / {
            proxy_pass http://app_servers;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host \$server_name;
        }
    }
}
EOF

echo -e "\n${BLUE}[3/5] Membangun dan Menjalankan Container...${NC}"
docker-compose up -d --build

# Pastikan container running
echo -e "${BLUE}Menunggu container stabil...${NC}"
sleep 15

if ! docker ps | grep -q "nginx"; then
    echo -e "\033[0;31mError: Container Nginx tidak berjalan. Mengecek log...${NC}"
    docker-compose logs nginx
    exit 1
fi

echo -e "\n${BLUE}[4/5] Menginstal SSL Certbot untuk $DOMAIN...${NC}"
# Jalankan certbot
certbot certonly --webroot -w .data/CTFd/uploads --email $EMAIL -d $DOMAIN --agree-tos --no-eff-email --non-interactive

# Cek apakah sertifikat berhasil dibuat
SSL_PATH="/etc/letsencrypt/live/$DOMAIN"
if [ -d "$SSL_PATH" ]; then
    echo -e "${GREEN}SSL Berhasil Diinstal!${NC}"
    
    # Update Nginx ke HTTPS
    cat > ./conf/nginx/http.conf <<EOF
worker_processes 4;
events { worker_connections 1024; }
http {
    upstream app_servers { server ctfd:8000; }
    server {
        listen 80;
        server_name $DOMAIN;
        return 301 https://\$host\$request_uri;
    }
    server {
        listen 443 ssl;
        server_name $DOMAIN;
        ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;
        
        client_max_body_size 4G;
        location /events {
            proxy_pass http://app_servers;
            proxy_set_header Connection '';
            proxy_http_version 1.1;
            chunked_transfer_encoding off;
            proxy_buffering off;
            proxy_cache off;
            proxy_redirect off;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host \$server_name;
        }
        location / {
            proxy_pass http://app_servers;
            proxy_redirect off;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host \$server_name;
        }
    }
}
EOF
    # Restart Nginx container
    docker-compose restart nginx
else
    echo -e "\033[0;31mGagal menginstal SSL. Menggunakan koneksi HTTP standar agar tetap bisa diakses...${NC}"
    # Pastikan Nginx tetap running di port 80
    docker-compose restart nginx
fi

echo -e "\n${BLUE}[5/5] Mengimpor Tantangan Default...${NC}"
echo -e "Untuk mengimpor tantangan secara otomatis, Anda memerlukan API Token Admin."
echo -e "1. Login ke https://$DOMAIN/admin"
echo -e "2. Buka User Settings -> Access Tokens"
echo -e "3. Generate token baru dan masukkan di bawah ini."
read -p "Masukkan API Token Admin (Kosongkan jika ingin lewati): " TOKEN

if [ ! -z "$TOKEN" ]; then
    sed -i "s/GANTI_DENGAN_TOKEN_ADMIN_ANDA/$TOKEN/g" challenges/import_challenges.py
    sed -i "s|http://localhost:8000|https://$DOMAIN|g" challenges/import_challenges.py
    
    # Jalankan import di dalam container atau di host
    if command -v python3 &> /dev/null; then
        pip3 install requests &> /dev/null
        python3 challenges/import_challenges.py
    else
        echo "Python3 tidak ditemukan, lewati impor tantangan."
    fi
fi

echo -e "\n${BLUE}Selesai!${NC}"
echo -e "${GREEN}Website SMK NEGERI 1 TANJUNG LAGO CTF siap diakses di: https://$DOMAIN${NC}"
echo -e "Gunakan 'docker-compose logs -f' untuk melihat log sistem."
