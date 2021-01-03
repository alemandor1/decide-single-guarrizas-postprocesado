from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods


class PostProcTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)

    def tearDown(self):
        self.client = None

    def test_identity(self):
        data = {
            'type': 'IDENTITY',
            'options': [
                { 'option': 'Option 1', 'number': 1, 'votes': 5 },
                { 'option': 'Option 2', 'number': 2, 'votes': 0 },
                { 'option': 'Option 3', 'number': 3, 'votes': 3 },
                { 'option': 'Option 4', 'number': 4, 'votes': 2 },
                { 'option': 'Option 5', 'number': 5, 'votes': 5 },
                { 'option': 'Option 6', 'number': 6, 'votes': 1 },
            ]
        }

        expected_result = [
            { 'option': 'Option 1', 'number': 1, 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 5', 'number': 5, 'votes': 5, 'postproc': 5 },
            { 'option': 'Option 3', 'number': 3, 'votes': 3, 'postproc': 3 },
            { 'option': 'Option 4', 'number': 4, 'votes': 2, 'postproc': 2 },
            { 'option': 'Option 6', 'number': 6, 'votes': 1, 'postproc': 1 },
            { 'option': 'Option 2', 'number': 2, 'votes': 0, 'postproc': 0 },
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)

    def test_multi_preguntas(self):
        data = {
            'type': 'MULTIPREGUNTAS',
            'questions': [
                [
                    { 'option': 'Option 1', 'number': 1, 'votes': 7 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 2 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 0 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 9 }
                ],
                [
                    { 'option': 'Option 1', 'number': 1, 'votes': 0 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 4 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 6 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 1 },
                    { 'option': 'Option 5', 'number': 5, 'votes': 7 }
                ],
            ]
        }

        expected_result = [
            [
                    { 'option': 'Option 4', 'number': 4, 'votes': 9, 'postproc': 9 },
                    { 'option': 'Option 1', 'number': 1, 'votes': 7, 'postproc': 7 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 2, 'postproc': 2 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 0, 'postproc': 0 }
                ],
                [
                    { 'option': 'Option 5', 'number': 5, 'votes': 7, 'postproc': 7 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 6, 'postproc': 6 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 4, 'postproc': 4 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 1, 'postproc': 1 },
                    { 'option': 'Option 1', 'number': 1, 'votes': 0, 'postproc': 0 }
                ],
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)

    def test_multi_preguntas2(self):
        data = {
            'type': 'MULTIPREGUNTAS',
            'questions': [
                [
                    { 'option': 'Option 1', 'number': 1, 'votes': 2 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 6 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 3 }
                ],
                [
                    { 'option': 'Option 1', 'number': 1, 'votes': 1 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 4 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 3 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 1 },
                    { 'option': 'Option 5', 'number': 5, 'votes': 2 },
                    { 'option': 'Option 6', 'number': 6, 'votes': 0 }
                ],
                [
                    { 'option': 'Option 1', 'number': 1, 'votes': 3 },
                    { 'option': 'Option 2', 'number': 2, 'votes': 8 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 0 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 0 }
                ],
            ]
        }

        expected_result = [
            [
                    { 'option': 'Option 2', 'number': 2, 'votes': 6, 'postproc': 6 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 3, 'postproc': 3 },
                    { 'option': 'Option 1', 'number': 1, 'votes': 2, 'postproc': 2 }
                ],
                [
                    { 'option': 'Option 2', 'number': 2, 'votes': 4, 'postproc': 4 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 3, 'postproc': 3 },
                    { 'option': 'Option 5', 'number': 5, 'votes': 2, 'postproc': 2 },
                    { 'option': 'Option 1', 'number': 1, 'votes': 1, 'postproc': 1 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 1, 'postproc': 1 },
                    { 'option': 'Option 6', 'number': 6, 'votes': 0, 'postproc': 0 }
                ],
                [
                    { 'option': 'Option 2', 'number': 2, 'votes': 8, 'postproc': 8 },
                    { 'option': 'Option 1', 'number': 1, 'votes': 3, 'postproc': 3 },
                    { 'option': 'Option 3', 'number': 3, 'votes': 0, 'postproc': 0 },
                    { 'option': 'Option 4', 'number': 4, 'votes': 0, 'postproc': 0 }
                ],
        ]

        response = self.client.post('/postproc/', data, format='json')
        self.assertEqual(response.status_code, 200)

        values = response.json()
        self.assertEqual(values, expected_result)
