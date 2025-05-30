from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Reservation
from django.utils import timezone
from datetime import timedelta, date, time


class BookingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="bookuser", password="testpass")
        self.book = Book.objects.create(
            title="Test Book",
            content="Welcome to the booking page."
        )
        self.reservation = Reservation.objects.create(
            user=self.user,
            guest_name="John Doe",
            guest_phone="1234567890",
            requested_date=date.today() + timedelta(days=1),
            requested_time=time(19, 0),
            seats=2,
            status="pending"
        )

    def test_book_str(self):
        """Test Book model __str__ output"""
        self.assertEqual(str(self.book), "Test Book")

    def test_reservation_str(self):
        """Test Reservation model __str__ output"""
        expected_str = f"bookuser | John Doe - {
            self.reservation.requested_date} @ {
                self.reservation.requested_time}"
        self.assertEqual(
            str(self.reservation), expected_str)

    def test_create_reservation(self):
        """Test reservation submission via POST"""
        self.client.login(username="bookuser", password="testpass")
        response = self.client.post(reverse('book'), {
            'requested_date': (
                timezone.now().date() + timedelta(days=2)),
            'requested_time': '18:00',
            'seats': 4
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Reservation.objects.filter(
                user=self.user).count(), 2)

    def test_delete_reservation(self):
        """Test deletion of reservation"""
        self.client.login(username="bookuser", password="testpass")
        response = self.client.post(
            reverse('book'), {'delete_id': self.reservation.id})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Reservation.objects.filter(
                id=self.reservation.id).exists())

    def test_edit_reservation(self):
        """Test editing a reservation"""
        self.client.login(username="bookuser", password="testpass")
        response = self.client.post(reverse('book'), {
            'edit_id': self.reservation.id,
            'requested_date': (
                timezone.now().date() + timedelta(days=3)),
            'requested_time': '20:00',
            'seats': 5
        })
        self.assertEqual(response.status_code, 302)
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.seats, 5)
