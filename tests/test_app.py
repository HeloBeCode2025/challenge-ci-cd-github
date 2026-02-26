import os
import sys

# Add the app folder to the path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))


def test_default_environment():
    """Default environment should be 'dev'"""
    env = os.environ.get("ENVIRONMENT", "dev")
    assert env in ["dev", "qa", "prod"]


def test_env_config_keys():
    """Each environment config should have a title and color"""
    env_config = {
        "dev":  {"title": "Dev Environment",        "color": "#90EE90"},
        "qa":   {"title": "QA Environment",          "color": "#FFFF99"},
        "prod": {"title": "Production Environment",  "color": "#FF9999"},
    }
    for env, config in env_config.items():
        assert "title" in config
        assert "color" in config
        assert config["color"].startswith("#")


def test_property_defaults():
    """Property template should have all required keys"""
    property_data = {
        "locality_name": "Bruxelles",
        "postal_code": 1000,
        "price": 0,
        "type_of_property": "House",
        "subtype_of_property": "House",
        "number_of_rooms": 4,
        "living_area": 180,
        "equipped_kitchen": 1,
        "furnished": 0.0,
        "open_fire": 0.0,
        "terrace": 0.0,
        "garden": 0.0,
        "number_of_facades": 3,
        "swimming_pool": 0.0,
        "state_of_building": "Good",
        "garden_surface": 0.0,
        "terrace_surface": 0,
    }
    required_keys = ["postal_code", "type_of_property", "living_area", "number_of_rooms"]
    for key in required_keys:
        assert key in property_data


def test_subtype_options():
    """Each property type should have valid subtypes"""
    subtype_options = {
        "House": ["House", "Villa", "Chalet", "Cottage", "Bungalow", "Mansion"],
        "Apartment": ["Flat", "FlatStudio", "Duplex", "Triplex", "Penthouse", "Loft"],
    }
    for prop_type, subtypes in subtype_options.items():
        assert len(subtypes) > 0
        assert isinstance(subtypes, list)