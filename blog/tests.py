from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment


class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='password123')
        self.post = Post.objects.create(
            title='Sample Post',
            slug='sample-post',
            author=self.user,
            content='This is a sample post.',
            status=1,
            is_active=True
        )

    def test_inactive_post_not_in_list(self):
        """Ensure inactive posts are not shown on the homepage"""
        self.post.is_active = False
        self.post.save()
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Sample Post')

    def test_draft_post_not_shown(self):
        """Ensure draft posts are not shown in views"""
        self.post.status = 0
        self.post.save()
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Sample Post')

    def test_post_str_method(self):
        """Check the __str__ method of Post"""
        self.assertEqual(
            str(self.post), 'Sample Post | written by testuser')

    def test_comment_model_str(self):
        """Check __str__ method for Comment"""
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='Nice article!',
            approved=True
        )
        self.assertEqual(
            str(comment), 'Comment Nice article! by testuser')
