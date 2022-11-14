import requests


class Personas:
    """
    Class to manage personas in the facebook
    application for the ampalibe project.
    """

    def __init__(self, page_id, access_token):
        self.page_id = page_id
        self.access_token = access_token
        self.url = "https://graph.facebook.com/v2.8"

    def list_personas(self):
        """
        Get the list personas of the page.
        """
        url = f"{self.url}/{self.page_id}/personas?access_token={self.access_token}"
        r = requests.get(url)
        return r.json()

    def get_persona(self, persona_id):
        """
        Get a persona of the page.
        """
        url = f"{self.url}/{persona_id}?access_token={self.access_token}"
        r = requests.get(url)
        return r.json()

    def create_persona(self, name, profile_picture_url):
        """
        Create a persona for the page.
        """
        url = f"{self.url}/{self.page_id}/personas?access_token={self.access_token}"
        data = {
            "name": name,
            "profile_picture_url": profile_picture_url,
        }
        r = requests.post(url, data=data)
        return r.json()

    def delete_persona(self, persona_id):
        """
        Delete a persona of the page.
        """
        url = f"{self.url}/{persona_id}?access_token={self.access_token}"
        r = requests.delete(url)
        return r.json()
