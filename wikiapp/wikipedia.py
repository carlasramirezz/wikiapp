import click
import requests
from pydantic import BaseModel, ValidationError

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


class Page(BaseModel):
    "A page dataclass to represent the return value from Wikipedia"

    title: str  # Title of Wikipedia page
    extract: str  # Extract of Wikipedia page


def random_page(
    language: str = "en",  # The language you want to use, as a two character string.
) -> Page:  # Returns a page object.
    """Get a random page from Wikipedia."""
    try:
        with requests.get(API_URL.format(language=language), timeout=10) as response:
            response.raise_for_status()
            data = response.json()
            return Page(**data)
        return data
    except (requests.RequestException, ValidationError) as error:
        message = str(error)
        raise click.ClickException(message) from error


# todo: handle clicks in console.py not here
