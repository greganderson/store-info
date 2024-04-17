import json

from fastapi.testclient import TestClient
import pytest

from main import app


client = TestClient(app)


@pytest.fixture
def store_list():
    with open("store_items.json") as f:
        return json.load(f)

def test_main(store_list: list[dict]):
    response = client.get("/items")
    result = response.json()
    for item in store_list:
        for actual_item in result:
             if item["id"] == actual_item["id"]:
                assert len(item) == len(actual_item)
                for key, value in item.items():
                    assert value == actual_item[key]
