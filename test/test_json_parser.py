import json
import pytest

@pytest.fixture
def json_content():
  return {
    "bunnies": "fluffy",
    "dogs": "adorable"
  }

@pytest.fixture
def config_file(tmp_path, json_content):
    file = tmp_path / "cute_things.json"
    try:
        with open(file, "w") as f:
            json.dump(json_content, f)
        yield (str(file))
    finally:
        file.unlink()

def test_temp_file(config_file, json_content):
    found = json.load(open(config_file, "r"))
    assert found == json_content