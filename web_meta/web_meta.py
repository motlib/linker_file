import logging

import requests
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


def _get_contents(url, max_size=8192, timeout=5):
    data = ''
    size = 0

    # open connection to the url
    with requests.get(url, timeout=timeout, stream=True) as response:

        # download chunks until max_size is reached
        for chunk in response.iter_content(chunk_size=1024, decode_unicode=True):
            data += chunk
            size += len(chunk)

            logging.warning(f'Downloaded chunk from {url}. Size is now {size}.')

            if size > max_size:
                break

    return data


def find_website_meta(url, timeout=5):
    '''Retrieve the url and try to extract metadata. Returns a dict with the
    extracted metadata. '''

    metadata = {}

    try:
        metadata['url'] = url

        response_text = _get_contents(url)

        # we take the HTML parser included with python
        soup = BeautifulSoup(response_text, "html.parser")

        # get website title
        metadata['title'] = soup.title.string
        #TODO: use og:title or twitter:title too

        # keywords
        tag = soup.find("meta",  {"property":"keywords"})
        metadata['keywords'] = tag['contents'] if tag else None

        # description
        tag = soup.find("meta",  {"property":"description"})
        metadata['description'] = tag['description'] if tag else None
        # todo: use og:description too

    except Exception as ex:
        logger.exception(f'Failed to retrieve website metadata for {url}.')

        metadata['error'] = str(ex)


    return metadata
