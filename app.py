from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transcript')
def transcript():

    video_id = request.args.get('videoId')

    try:

        api = YouTubeTranscriptApi()

        transcript_data = api.fetch(video_id)

        text = " ".join([x.text for x in transcript_data])

        return jsonify({
            "transcript": text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(port=5000)