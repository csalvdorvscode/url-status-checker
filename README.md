# 🌐 URL Status Checker

A Python tool that reads a list of URLs, removes duplicates, sends HTTP GET requests, and reports the HTTP status code for each website.

## 🚀 Features

- Reads URLs from `urls.txt`
- Removes duplicate URLs automatically
- Ignores blank lines
- Automatically adds `https://` if a protocol is missing
- Sends HTTP GET requests
- Reports HTTP status codes (200, 301, 403, 404, 500...)
- Handles connection errors and timeouts
- Fast and lightweight

## 🛠️ Tech Stack

- Python 3
- Requests

## 📥 Installation

```bash
pip install requests
```

## ▶️ Usage

1. Add your URLs to `urls.txt`
2. Run:

```bash
python main.py
```

## 📄 Example Output

```
Checking 5 unique URLs...

[200] -> https://google.com
[200] -> https://github.com
[404] -> https://httpbin.org/status/404
[403] -> https://httpbin.org/status/403
```
