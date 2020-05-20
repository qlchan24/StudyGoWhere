from django.test import TestCase, Client
from sgw.models import *
# Create your tests here. test method names have to start with "test_"


class locationDbTest(TestCase):

    def setUp(self):
        # create more test database objects if u want using the same format

        Location.objects.create(
            locationName="Hssml",
            openingTime="11:00",
            closingTime="12:00"
        )

        Location.objects.create(
            locationName="com1",
            openingTime="13:00",
            closingTime="19:00"
        )

        StudySpot.objects.create(
            description="hssml DR5",
            airConditioned=True,
            discussionFriendly=True,
            wallSockets=True,
            levelNumber=3,
            locationName=Location.objects.get(locationName="Hssml")
        )

        StudySpot.objects.create(
            description="com1 annex",
            airConditioned=True,
            discussionFriendly=False,
            wallSockets=True,
            levelNumber=2,
            locationName=Location.objects.get(locationName="com1")
        )

        Rating.objects.create(
            crowdedness=2,
            studyspot="com1 annex",
            whenRated="12:00"
        )

        self.client = Client()

    def test_indexview(self):
        response = self.client.get('/locations')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['locations'], ["com1", "Hssml"])

    def test_locationview(self):
        response = self.client.get('/locations/com1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['location'], "com1")
        self.assertEqual(response.context['levelNumber'], [2])
        self.assertEqual(response.context['openingTime'], 1300)
        self.assertEqual(response.context['closingTime'], 1900)

    def test_query(self):
        Rating.objects.filter(studyspot='com1 annex')
