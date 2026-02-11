import requests
import json
import os

# Konfigurasi API
CTFD_URL = "http://localhost:8000"  # Sesuaikan jika running di VPS
API_TOKEN = "GANTI_DENGAN_TOKEN_ADMIN_ANDA" # Token bisa didapat dari User Settings -> Access Tokens

def import_challenges():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    # List Tantangan SMK NEGERI 1 TANJUNG LAGO
    challenges = [
        {
            "name": "Web Dasar: Inspect Element",
            "category": "Web",
            "description": "Coba cari flag yang tersembunyi di dalam kode HTML halaman ini!",
            "value": 100,
            "type": "standard",
            "state": "visible",
            "flag": "SMKN1TL{1nsp3ct_3l3m3nt_is_fun}"
        },
        {
            "name": "Crypto: Caesar Cipher",
            "category": "Cryptography",
            "description": "Pesan rahasia: 'VTMRA1GY{P3m4_P3m4_P3m4}'. Geser 13 kali ke belakang.",
            "value": 150,
            "type": "standard",
            "state": "visible",
            "flag": "SMKN1TL{C3z4_C3z4_C3z4}"
        },
        {
            "name": "Misc: Telegram SMK",
            "category": "Misc",
            "description": "Join ke grup telegram admin di t.me/she0rif untuk mendapatkan flag.",
            "value": 50,
            "type": "standard",
            "state": "visible",
            "flag": "SMKN1TL{w3lc0m3_t0_th3_gr0up}"
        }
    ]

    for chal in challenges:
        print(f"Mengimpor: {chal['name']}...")
        
        # Create Challenge
        data = {
            "name": chal["name"],
            "category": chal["category"],
            "description": chal["description"],
            "value": chal["value"],
            "type": chal["type"],
            "state": chal["state"]
        }
        
        response = requests.post(f"{CTFD_URL}/api/v1/challenges", headers=headers, json=data)
        
        if response.status_code == 200:
            chal_id = response.json()["data"]["id"]
            
            # Add Flag
            flag_data = {
                "challenge_id": chal_id,
                "content": chal["flag"],
                "type": "static"
            }
            requests.post(f"{CTFD_URL}/api/v1/flags", headers=headers, json=flag_data)
            print(f"Sukses mengimpor {chal['name']}")
        else:
            print(f"Gagal mengimpor {chal['name']}: {response.text}")

if __name__ == "__main__":
    if API_TOKEN == "GANTI_DENGAN_TOKEN_ADMIN_ANDA":
        print("Error: Harap isi API_TOKEN terlebih dahulu di script import_challenges.py")
    else:
        import_challenges()
