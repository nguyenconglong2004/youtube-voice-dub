# Trích phụ đề từ YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

def get_transcript(video_id: str, lang_code: str = 'en'):
    """
    Lấy phụ đề của video YouTube.

    :param video_id: ID của video YouTube (ví dụ: 'dQw4w9WgXcQ')
    :param lang_code: Mã ngôn ngữ phụ đề (ví dụ: 'en', 'vi', 'a.en' với 'a.' là auto-generated)
    :return: Danh sách các đoạn phụ đề hoặc None nếu không lấy được
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])
        return transcript
    except TranscriptsDisabled:
        print("Phụ đề bị tắt cho video này.")
    except NoTranscriptFound:
        print(f"Không tìm thấy phụ đề với mã ngôn ngữ '{lang_code}'.")
    except VideoUnavailable:
        print("Video không tồn tại hoặc không khả dụng.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    return None

video_id = "nQdyiK7-VlQ"
lang = "en"  # hoặc "a.en" nếu bạn muốn phụ đề tự động tiếng Anh

transcript = get_transcript(video_id, lang)

if transcript:
    for item in transcript[:5]:  # chỉ in thử 5 đoạn đầu
        print(f"{item['start']:.2f}s - {item['end']:.2f}s: {item['text']}")
