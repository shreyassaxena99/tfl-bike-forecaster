import os
from supabase import create_client
from ingest_bikepoint import get_bikepoint_data

def main():
    if os.getenv("ENABLED", "false").lower() != "true":
        print("Ingest disabled. Set ENABLED=true to run.")
        return

    supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])
    data = get_bikepoint_data()
    supabase.table("raw_bikepoint_data").insert(data).execute()

if __name__ == "__main__":
    main()
