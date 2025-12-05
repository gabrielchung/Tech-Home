# Tech Home

**Tech Home** is a curated, long-term archive of high-quality engineering articles from leading technology companies.  
It is a peaceful, organized place to read, reflect, and grow in understanding. Our goal is to preserve knowledge that endures, rather than chasing fleeting news or hype.

---

## **Mission**

- Provide a **trustworthy and calm resource** for engineers, developers, and learners.  
- Focus on **wisdom and insight** from long-form articles, blog posts, and engineering case studies.  
- Maintain a **stable, long-term archive** that can be browsed, explored, and enriched over time.  
- Serve others faithfully by curating knowledge with **care, order, and clarity**.

---

## **Sources**

Currently, Tech Home archives articles from four high-quality engineering blogs:

| Source | URL | Coverage |
|--------|-----|----------|
| Google Developers | [https://developers.googleblog.com](https://developers.googleblog.com) | Web, Android, tools, ML |
| Microsoft Engineering | [https://devblogs.microsoft.com/engineering-at-microsoft/](https://devblogs.microsoft.com/engineering-at-microsoft/) | Azure, OS, dev tools |
| Apple Developer News | [https://developer.apple.com/news/](https://developer.apple.com/news/) | APIs, frameworks, OS updates |
| GitHub Blog | [https://github.blog](https://github.blog) | Developer workflows, open-source, tooling |

---

## **How It Works**

1. **Feeds**  
   - Each blog has an RSS/Atom feed that is fetched periodically.

2. **GitHub Actions Automation**  
   - A workflow runs weekly (or on-demand) to fetch new articles and append them to the archive JSON file.  
   - Versioning ensures history is preserved and changes are transparent.

3. **Archive Storage**  
   - Articles are stored in `data/articles.json` with metadata including title, source, URL, published date, tags, summary, and optional notes.  
   - The structure allows easy tagging, categorization, and eventual search or filtering.

4. **Local Curation**  
   - Articles can be manually tagged and annotated locally before or after syncing.

5. **Browsing**  
   - Users can browse the archive via a simple static webpage (planned) or inspect the JSON directly.

