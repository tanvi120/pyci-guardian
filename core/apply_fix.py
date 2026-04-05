def apply_fix_to_file(file_path: str, new_code: str):
    try:
        with open(file_path, "w") as f:
            f.write(new_code)

        print(f"✅ Applied fix to {file_path}")

    except Exception as e:
        print("❌ Failed to apply fix:", e)
