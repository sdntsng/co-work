#!/usr/bin/env python3
import sys
import shutil
import os
import json

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILES_DIR = os.path.join(BASE_DIR, "../profiles")
TARGET_CONFIG = os.path.expanduser("~/.gemini/antigravity/mcp_config.json")

def list_profiles():
    files = [f for f in os.listdir(PROFILES_DIR) if f.endswith('.json')]
    return [f.replace('.json', '') for f in files]

def switch_profile(profile_name):
    source_file = os.path.join(PROFILES_DIR, f"{profile_name}.json")
    
    if not os.path.exists(source_file):
        print(f"❌ Profile '{profile_name}' not found.")
        print("Available profiles:", ", ".join(list_profiles()))
        return False
    
    try:
        # Verify JSON validity before copying
        with open(source_file, 'r') as f:
            json.load(f)
            
        shutil.copy2(source_file, TARGET_CONFIG)
        print(f"✅ Switched to profile: {profile_name}")
        print(f"   (Config copied to {TARGET_CONFIG})")
        print("\n⚠️  PLEASE RESTART YOUR AGENT/CLIENT TO APPLY CHANGES.")
        return True
    except Exception as e:
        print(f"❌ Error switching profile: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python switch_profile.py [profile_name]")
        print("Available profiles:", ", ".join(list_profiles()))
        sys.exit(1)
        
    profile = sys.argv[1].lower()
    switch_profile(profile)
