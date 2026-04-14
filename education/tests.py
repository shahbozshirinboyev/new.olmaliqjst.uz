from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Assessment, Control


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class AssessmentViewTests(TestCase):
    def test_assessment_page_renders_assessment_and_control_separately(self):
        Assessment.objects.create(title='Baholash', content='Baholash matni')
        Control.objects.create(title='Nazorat', content='Nazorat matni')

        response = self.client.get(reverse('education:assessment'))

        self.assertContains(response, 'Baholash matni')
        self.assertContains(response, 'Nazorat matni')
