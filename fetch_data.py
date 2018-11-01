import json

import wikitables


def fetch_data(page):
    tables = wikitables.import_tables(page)

    for table in tables:
        for row in json.loads(table.json()):
            yield row


if __name__ == "__main__":
    print(list(fetch_data("List of Hi-NRG artists and songs")))
