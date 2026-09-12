# ----------------------------------------------------
# Day 24: Automatic File Organizer & Desktop Cleaner
# Concepts: os, shutil, pathlib, Dictionary Classification, File System Operations
# ----------------------------------------------------

import os
import shutil

EXTENSIONS_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code_and_Scripts": [".py", ".js", ".html", ".css", ".json", ".cpp", ".java", ".sh"]
}

def get_category_for_ext(extension):
    ext = extension.lower()
    for category, ext_list in EXTENSIONS_MAPPING.items():
        if ext in ext_list:
            return category
    return "Others"

def organize_directory(target_path, dry_run=False):
    if not os.path.exists(target_path):
        print(f"❌ Target path does not exist: {target_path}")
        return

    print("\n" + "=" * 55)
    mode_label = "🔍 PREVIEW (DRY RUN)" if dry_run else "🚀 ORGANIZING FILES"
    print(f"{mode_label}: {target_path}".center(55))
    print("=" * 55)

    items = os.listdir(target_path)
    moved_count = 0

    for item in items:
        item_path = os.path.join(target_path, item)

        # Skip subdirectories or hidden files
        if os.path.isdir(item_path) or item.startswith("."):
            continue

        _, ext = os.path.splitext(item)
        if not ext:
            continue

        category = get_category_for_ext(ext)
        dest_folder = os.path.join(target_path, category)
        dest_path = os.path.join(dest_folder, item)

        if dry_run:
            print(f"  [Preview] Would move: '{item}' -> '{category}/'")
        else:
            os.makedirs(dest_folder, exist_ok=True)
            # Avoid overwrite collision
            if os.path.exists(dest_path):
                base, ext_part = os.path.splitext(item)
                dest_path = os.path.join(dest_folder, f"{base}_copy{ext_part}")
            shutil.move(item_path, dest_path)
            print(f"  ✅ Moved: '{item}' -> '{category}/'")

        moved_count += 1

    print("-" * 55)
    if moved_count == 0:
        print("No unorganized files found in the directory.")
    else:
        print(f"Total files {'identified' if dry_run else 'organized'}: {moved_count}")
    print("=" * 55)

def create_sample_folder():
    sample_dir = "sample_messy_folder"
    os.makedirs(sample_dir, exist_ok=True)
    sample_files = [
        "report.pdf", "family_photo.jpg", "notes.txt", 
        "song.mp3", "video_clip.mp4", "archive.zip", "script.py"
    ]
    for sf in sample_files:
        with open(os.path.join(sample_dir, sf), "w") as f:
            f.write("Sample test content.")
    print(f"✅ Created test sample directory: '{sample_dir}' with {len(sample_files)} dummy files.")
    return sample_dir

def main():
    print("=" * 50)
    print("📁 AUTOMATIC FILE ORGANIZER 📁".center(50))
    print("=" * 50)

    print("1. Organize a Custom Directory (Enter path)")
    print("2. Create and Organize a Test Demo Folder")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        path = input("Enter full folder path to organize: ").strip()
        dry = input("Preview only (dry run)? [y/n, default n]: ").strip().lower() == "y"
        organize_directory(path, dry_run=dry)
    elif choice == "2":
        sample_path = create_sample_folder()
        print("\nStep 1: Previewing file movements...")
        organize_directory(sample_path, dry_run=True)
        proceed = input("\nProceed with actual organizing? (y/n): ").strip().lower()
        if proceed in ("y", "yes"):
            organize_directory(sample_path, dry_run=False)
    elif choice == "3":
        print("\nGoodbye! Keep your files organized! 🗄️\n")

if __name__ == "__main__":
    main()
