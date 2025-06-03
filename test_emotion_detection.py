from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        """I am glad this happened → joy"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result.get('dominant_emotion'), 'joy')

    def test_anger(self):
        """I am really mad about this → anger"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result.get('dominant_emotion'), 'anger')

    def test_disgust(self):
        """I feel disgusted just hearing about this → disgust"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result.get('dominant_emotion'), 'disgust')

    def test_sadness(self):
        """I am so sad about this → sadness"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result.get('dominant_emotion'), 'sadness')

    def test_fear(self):
        """I am really afraid that this will happen → fear"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result.get('dominant_emotion'), 'fear')

if __name__ == '__main__':
    unittest.main()


