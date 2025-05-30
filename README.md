# 🔍 Web Scraping Wizardry with Beautiful Soup 🧙♂️

![Web Scraping Illustration](https://img.icons8.com/color/96/000000/data-configuration.png)


## 🌟 Features

### Local HTML Scraper
- Scrapes course info from `test.html`
- Extracts:
  - 📚 Course titles
  - 💰 Pricing info
- Uses BeautifulSoup's `find_all()` to get all cards

### 🔥 Live Job Scraper
- Searches [TimesJobs](https://m.timesjobs.com) in real-time
- Filters jobs by your desired skill
- Exports to clean CSV format
- Shows:
  - 👔 Job title
  - 🏢 Company
  - ⏰ Posting time
  - 🛠️ Required skills

## 🚀 Quick Start

```bash
pip install beautifulsoup4 requests lxml
python job_scraper.py
```

When prompted, enter your desired skill:
```
What skill do you wanna filter for? 
> python
```

## 📊 Sample Output

```
=JOB ROLE= Python Developer =AT= TechWizards Inc. =POSTED AT= 1 hour ago
Skills: Python, Flask, Django, AWS
--------------------------------------------------
```

![CSV Export Screenshot](https://img.icons8.com/color/48/000000/ms-excel.png) Jobs saved to `Jobs.csv`

## 💡 Pro Tips

```python
# Use these secret techniques:
soup.find_all('div', class_='card')  # Finds all cards
[job.text.strip() for job in jobs]   # Clean list comprehension
```

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-green)
![Requests](https://img.shields.io/badge/Requests-HTML-red)

## 📜 License

MIT License - scrape responsibly!

---
### Happy Scraping! 🎉

Made with ❤️ by [Assia] | [![Twitter](https://img.icons8.com/color/24/000000/twitter.png)](https://twitter.com/yourhandle)
https://x.com/BoussanniEl



