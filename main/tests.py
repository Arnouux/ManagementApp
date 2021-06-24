from django.http import response
from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Reservation, Tool
from django.contrib.auth.models import User

class ToolModelTests(TestCase):

    def setUp(self):
        Tool.objects.create(name="tool_test")

    def test_no_reservation_at_first(self):
        """
        Tool should have no reservation at first.
        """
        tool = Tool.objects.get(name="tool_test")
        self.assertFalse(tool.dates.all().exists())

    def test_add_reservation_to_tool(self):
        """
        Create a Reservation should make one in the tool.dates.
        """
        tool = Tool.objects.get(name="tool_test")
        reservation = Reservation(start_date=timezone.now(),
                        end_date=timezone.now() + datetime.timedelta(days=30),
                        by_who="ARAR",
                        tool=tool)

        reservation.save()
        self.assertTrue(tool.dates.all().exists())


class MainViewTests(TestCase):

    response = response.HttpResponse()

    def setUp(self) -> None:
        """
        Setup a connection
        """
        self.client.post(reverse('login'), {'name':"ARAR"})
        self.response = self.client.get(reverse('index'))
    
    def test_main_view(self):
        """
        Main page without tool in DB should print "No tools".
        """
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "No tools are available.")
    
    def test_main_view_with_tool(self):
        """
        Main page with tools in DB should print them.
        """
        Tool.objects.create(name="tool_test")
        self.response = self.client.get(reverse('index'))
        self.assertContains(self.response, "tool_test")

class MainViewNotConnected(TestCase):
    def test_not_connected_then_redirected(self):
        """
        Accessing main page while not connected should redirect (302)
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)


class LoginViewTests(TestCase):
    def test_connect(self):
        """
        Connecting should redirect (302)
        Reloading the main page should now be OK (200)
        """
        response = self.client.post(reverse('login'), {'name':"ARAR"})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class UserTests(TestCase):
    def test_connect(self):
        """
        TODO : test Users
        """
        User.objects.create(username="username")
        print(User.objects.get(username="username"))

        Tool.objects.create(name="tool_test")
        tool = Tool.objects.get(name="tool_test")
        print(tool)
        Reservation.objects.create(start_date=timezone.now(),
                            end_date=timezone.now() + datetime.timedelta(days=30),
                            by_who="ARAR",
                            tool=tool)
        
        Reservation.objects.create(start_date=timezone.now()+ datetime.timedelta(days=20),
                            end_date=timezone.now() + datetime.timedelta(days=40),
                            by_who="JUBO",
                            tool=tool)
        r = Reservation.objects.get(by_who="ARAR")
        print(r)
        print(tool)