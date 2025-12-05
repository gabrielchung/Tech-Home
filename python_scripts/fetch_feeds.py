import json
import feedparser
from datetime import datetime
from pathlib import Path

# Load feed list
with open("feed_sources/feeds.json") as f:
    feeds = json.load(f)

# Determine current month
now = datetime.utcnow()
month_str = f"{now.year}-{now.month:02}"

# Helper to get folder name from feed
def folder_name(feed_name):
    name_map = {
        "Google Developers": "google",
        "Microsoft Engineering": "microsoft",
        "Apple Developer News": "apple",
        "GitHub Blog": "github"
    }
    return name_map.get(feed_name, feed_name.lower().replace(" ", "_"))

# Load or initialize the "all" archive
all_folder = Path("data/all")
all_file = all_folder / f"{month_str}.json"
if all_file.exists():
    with all_file.open() as f:
        all_archive = json.load(f)
else:
    all_archive = {"articles": []}
all_ids = {a['id'] for a in all_archive['articles']}

for feed in feeds:
    folder = Path(f"data/{folder_name(feed['name'])}")
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"{month_str}.json"

    # Load or initialize per-feed archive
    if file_path.exists():
        with file_path.open() as f:
            feed_archive = json.load(f)
    else:
        feed_archive = {"articles": []}
    feed_ids = {a['id'] for a in feed_archive['articles']}

    parsed = feedparser.parse(feed['url'])
    new_articles_feed = []
    new_articles_all = []

    for entry in parsed.entries:
        article_id = entry.id if 'id' in entry else entry.link
        if article_id not in feed_ids:
            article = {
                "id": article_id,
                "title": entry.title,
                "source": feed['name'],
                "url": entry.link,
                "published_at": entry.published if 'published' in entry else "",
                "fetched_at": now.isoformat(),
                "tags": [],
                "summary": entry.summary if 'summary' in entry else "",
                "notes": ""
            }
            feed_archive['articles'].append(article)
            feed_ids.add(article_id)
            new_articles_feed.append(article)

        if article_id not in all_ids:
            all_archive['articles'].append(article)
            all_ids.add(article_id)
            new_articles_all.append(article)

    # Save per-feed archive
    with file_path.open("w") as f:
        json.dump(feed_archive, f, indent=2)

# Save combined archive
all_folder.mkdir(parents=True, exist_ok=True)
with all_file.open("w") as f:
    json.dump(all_archive, f, indent=2)

print("Archives updated:")
for feed in feeds:
    print(f"- {folder_name(feed['name'])} folder")
print(f"- all folder ({len(all_archive['articles'])} articles)")
