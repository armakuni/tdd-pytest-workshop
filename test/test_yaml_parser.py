import pytest
import yaml


@pytest.fixture
def example_yaml(example_dict):
    return yaml.safe_dump(example_dict)


@pytest.fixture
def config_file(tmp_path, example_yaml):
    file = tmp_path / "cute_things.yaml"
    try:
        file.write_text(example_yaml)
        yield str(file)
    finally:
        file.unlink()


def test_yaml_parser(config_file, example_dict):
    expected = example_dict
    actual = yaml_parser(config_file)
    assert actual == expected


def yaml_parser(file):
    with open(file) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)
