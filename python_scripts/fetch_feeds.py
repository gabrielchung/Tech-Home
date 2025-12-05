import json
import feedparser
from datetime import datetime

# Load feed list
with open("feed_sources/feeds.json") as f:
    feeds = json.load(f)

# Load existing articles
with open("data/articles.json") as f:
    archive = json.load(f)

existing_ids = {a['id'] for a in archive['articles']}

new_articles = []

for feed in feeds:
    parsed = feedparser.parse(feed['url'])
    for entry in parsed.entries:
        article_id = entry.id if 'id' in entry else entry.link
        if article_id not in existing_ids:
            article = {
                "id": article_id,
                "title": entry.title,
                "source": feed['name'],
                "url": entry.link,
                "published_at": entry.published if 'published' in entry else "",
                "fetched_at": datetime.utcnow().isoformat(),
                "tags": [],
                "summary": entry.summary if 'summary' in entry else "",
                "notes": ""
            }
            new_articles.append(article)
            existing_ids.add(article_id)

# Append new articles to archive
archive['articles'].extend(new_articles)

with open("data/articles.json", "w") as f:
    json.dump(archive, f, indent=2)

print(f"Added {len(new_articles)} new articles")
