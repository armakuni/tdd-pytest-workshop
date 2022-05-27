import json

import pytest


@pytest.fixture
def example_json(example_dict):
    return json.dumps(example_dict)


@pytest.fixture
def config_file(tmp_path, example_json):
    file = tmp_path / "cute_things.json"
    try:
        file.write_text(example_json)
        yield str(file)
    finally:
        file.unlink()


def test_json_parser(config_file, example_dict):
    expected = example_dict
    actual = json_parser(config_file)
    assert actual == expected


def json_parser(json_file):
    with open(json_file) as f:
        return json.loads(f.read())
