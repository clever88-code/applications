from django.test import TestCase
from django.utils import timezone
from core.models import Status, AuthUser, office, Application, Labs_cabinets
from django.contrib.auth.models import User

class StatusModelTest(TestCase):
    def test_string_representation(self):
        status = Status.objects.create(name="Test Status")
        self.assertEqual(str(status), "Test Status")

class AuthUserModelTest(TestCase):
    def test_string_representation(self):
        auth_user = AuthUser.objects.create(username="testuser")
        self.assertEqual(str(auth_user), "testuser")

class OfficeModelTest(TestCase):
    def test_string_representation(self):
        office = office.objects.create(number="123")
        self.assertEqual(str(office), "123")

class ApplicationModelTest(TestCase):
    def create_application(self):
        status = Status.objects.create(name="New Status")
        auth_user = AuthUser.objects.create(username="user")
        office = office.objects.create(number="123")
        worker = User.objects.create(username="worker", groups="labs")
        return Application.objects.create(
            date=timezone.now(),
            auth_user=auth_user,
            number_cab=office,
            description="Test description",
            status_application=status,
            worker=worker,
            comments="Test comment"
        )

    def test_string_representation(self):
        application = self.create_application()
        self.assertEqual(
            str(application),
            f'№{application.id} каб.{application.number_cab} Заявитель {application.auth_user}'
        )

class LabsCabinetsModelTest(TestCase):
    def create_labs_cabinet(self):
        office = office.objects.create(number="123")
        worker = User.objects.create(username="worker", groups="labs")
        return Labs_cabinets.objects.create(
            cabinet=office,
            worker=worker
        )

    def test_string_representation(self):
        labs_cabinet = self.create_labs_cabinet()
        self.assertEqual(
            str(labs_cabinet),
            f'Кабинет {labs_cabinet.cabinet} привязан к лаборату {labs_cabinet.worker}'
        )
