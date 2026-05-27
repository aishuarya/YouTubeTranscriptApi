# YouTube Transcript Service

Extracts YouTube video transcripts using `youtube-transcript-api`.

# Run Application

```bash
python app.py
```

Server starts on:

```text
http://localhost:5000
```

---

# API Endpoint

## GET /transcript

Extract transcript from a YouTube video.

### Request

```text
GET /transcript?videoId=VIDEO_ID
```

# Success Response

```json
{
  "transcript": "Long transcript text..."
}
```

---
