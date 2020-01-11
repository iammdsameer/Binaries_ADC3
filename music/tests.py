# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from .models import Animal

# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')
from django.test import TestCase
from .models import Music

class MusicTestCase(TestCase):
    def setUp(self):
        Music.objects.create(music_title='Main Hoon Naa',music_artist="Emiway Bantai", music_album="Machaynge",music_coverArt="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.mid-day.com%2Fimages%2F2019%2Fjan%2FEmiway-Rapper_d.jpg&f=1&nofb=1", music_file="Allare Nani Keshi     .mp3", music_length=10)

    def test_music_gets_adopted(self):
        test1 = Music.objects.get(music_title="Main Hoon Na")
        self.assertEqual(test1.music_album(), "Machaynge")