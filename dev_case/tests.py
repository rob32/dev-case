from django.test import TestCase

# TODO: add more tests + refactor


class DefaultPageTest(TestCase):
    def test_home_view_with_inital_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Welcome...")

    def test_about_view_with_inital_template(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
        self.assertContains(response, "About")

    def test_search_view_with_inital_template(self):
        response = self.client.get("/search/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search.html")
        self.assertContains(response, "Search")


class SitemapTest(TestCase):
    def test_inital_sitemap(self):
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/xml")


class RobotsTest(TestCase):
    def test_robots_txt_without_extra_rules(self):
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "robots.txt")
        self.assertEqual(response["content-type"], "text/plain")
