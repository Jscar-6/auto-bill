from pathlib import Path
import json

file_path = Path(__file__).parent / "fixtures" / "threads.json"

with open(file_path, "r") as file:
    emails = json.load(file)

print(f"Loaded {len(emails)} emails from {file_path.name}\n")

threads = {}
for email in emails:
    threads.setdefault(email["thread_id"], []).append(email)

for thread_id, messages in sorted(threads.items()):
    messages.sort(key=lambda m: m["sent_time"])
    subject = messages[0]["subject"]
    total_chars = sum(len(m["body"]) for m in messages)

    print(f"Thread {thread_id}: {subject}")
    print(f"  {len(messages)} message(s), {total_chars} chars")
    for m in messages:
        print(f"    {m['sent_time']}  {m['sender']}")
    print()
