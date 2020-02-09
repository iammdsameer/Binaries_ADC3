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
from .models import Artists, Musics, Distributors, Albums


class MusicTestCase(TestCase):
    def setUp(self):
        Artists.objects.create(
            name='Anil', image='https://anilpoudyal.com.np/')
        Musics.objects.create(music_title='Aama le sodhlin ni', music_coverArt="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.mid-day.com%2Fimages%2F2019%2Fjan%2FEmiway-Rapper_d.jpg&f=1&nofb=1",
                              music_file="Aama le sodhlin ni     .mp3", music_length=12)
        Distributors.objects.create(
            name='OSR Digital', logo='https://osrdigital.com.np/')
        Albums.objects.create(album_title='Machayange',
                              album_logo="https://emiway.com/logo/")

    def testArtist(self):
        testArtist = Artists.objects.get(name="Anil")
        self.assertEqual(testArtist.name, "Anil")

    def testMusic(self):
        testMusic = Musics.objects.get(music_title="Aama le sodhlin ni")
        self.assertEqual(testMusic.music_title, "Aama le sodhlin ni")

    def testDistributors(self):
        testDistributors = Distributors.objects.get(name="OSR Digital")
        self.assertEqual(testDistributors.name, "OSR Digital")

    def testAlbums(self):
        testAlbums = Albums.objects.get(album_title="Machayange")
        self.assertEqual(testAlbums.album_title, "Machayange")
