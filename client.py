import requests


class Client:
    def __init__(self, postcode: str = None) -> None:
        self._postcode = postcode
        self.reference = "https://uk.api.just-eat.io/restaurants/bypostcode/"
        self.header = {
            "Content-Type": "application/json",
            "User-Agent": ("Chrome/117.0.0.0 Safari/537.36")
        }
        self.restaurants = []


    @property
    def postcode(self) -> str:
        return self._postcode

    @postcode.setter
    def postcode(self, postcode: str) -> None:
        self._postcode = postcode
        self.restaurants = self.get_restaurants()

    def get_restaurants(self) -> list:

        try:
            response = requests.get(f"{self.reference}{self._postcode}", headers=self.header)
            response.raise_for_status()

            data = response.json()

            self.restaurants = [
                {"Name": restaurant["Name"],
                 "Rating": restaurant["RatingStars"],
                 "Cuisines": [cuisine["Name"] for cuisine in restaurant["Cuisines"]]
                 } for restaurant in data["Restaurants"]
            ]

            return self.restaurants

        except requests.HTTPError as e:
            raise f"HTTP error: {str(e)}"

        except requests.RequestException as e:
            raise f"Request error: {str(e)}"
