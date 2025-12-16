"""Unit tests for EmotionDetection package"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test class for emotion detection"""

    def test_emotion_detection(self):
        """Test emotion detection capabilities of the package"""

        tests = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]

        for item in tests:
            # Find dominant emotion of the current test case
            dominant_emotion = emotion_detector(item[0])['dominant_emotion']

            # Assert it's equal the expected emotion
            self.assertEqual(dominant_emotion, item[1])

unittest.main()
