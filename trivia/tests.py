from django.test import TestCase

class LinkCheckTestCase(TestCase):

    def test_shows_login(self):
        response = self.client.get('/')
        self.assertContains(response, 'Login Page')

    def test_shows_game_page(self):
        response = self.client.get('/game/')
        self.assertContains(response, 'get started!')

    def test_shows_incorrect_page(self):
        response = self.client.get('/game/incorrect/')
        self.assertContains(response, 'Sorry!')

    def test_shows_correct_page(self):
        response = self.client.get('/game/correct/')
        self.assertContains(response, 'CORRECT!!!')