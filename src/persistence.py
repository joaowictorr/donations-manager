import json
import os

STORAGE_FILE = "donations.json"

def save_donations(donation_list):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump([d.to_dict() for d in donation_list], f, indent=4)

def load_donations():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        from src.donation import Donation
        return [
            Donation(d["item_name"], d["quantity"], d["expiration_date"]) 
            for d in data
        ]