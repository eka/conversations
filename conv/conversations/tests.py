"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from conversations.models import Conversation, Message
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    def setUp(self):
        # create 3 users
        self.user1 = User.objects.create(username='user1', email='user1@a.com', password='nada')
        self.user2 = User.objects.create(username='user2', email='user2@a.com', password='nada')
        self.user3 = User.objects.create(username='user3', email='user3@a.com', password='nada')

    def test_conversation(self):
        user1 = User.objects.get(username=self.user1.username)
        self.assertTrue(user1)
        c1 = Conversation()
        c1.save()
        c1.users.add(self.user1)
        c1.users.add(self.user2)
        c1.users.add(self.user3)

        self.assertEqual(3, c1.users.count())

        m1 = Message.objects.create(user=self.user1, text='hi')
        m2 = Message.objects.create(user=self.user1, text='hi there')
        c1.messages.add(m1)
        c1.messages.add(m2)

        self.assertEqual(2, c1.messages.count())

