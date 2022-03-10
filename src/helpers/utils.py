import inspect
import os
import os.path
import random
import string
import sys
import urllib.parse


def get_root_path(follow_symlinks=True) -> str:
    if getattr(sys, 'frozen', False):
        _path = os.path.abspath(sys.executable)
    else:
        _path = inspect.getabsfile(get_root_path)
    if follow_symlinks:
        _path = os.path.realpath(_path)
    parts = os.path.dirname(_path).split(os.path.sep)
    _path = os.path.sep.join(parts[:-2])
    return _path


def get_url(base_url: str, endpoint: str) -> str:
    return urllib.parse.urljoin(base_url, endpoint)


def get_random_string(length=8, upper_case=False, numbers=False, special=False) -> str:
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    if upper_case:
        random_string = random.choice(string.ascii_uppercase) + random_string[:-1]
    if numbers:
        random_string = random.choice("1234567890") + random_string[:-1]
    if special:
        random_string = random.choice("!@#$%^*-_+=") + random_string[:-1]
    return random_string


def get_file_data(file_name: str) -> str:
    try:
        f = open(file_name, "r")
        strings = f.read().replace('\n', '')
        f.close()
    except:
        strings = ""
    return strings


def write_data(file_name: str, data: str):
    try:
        f = open(file_name, "w")
        f.write(data)
        f.close()
    except:
        pass


def get_versions(version_range: str) -> (str, str):
    ver = version_range \
        .replace("[,", "[0,") \
        .replace("-", ",") \
        .replace("<", "") \
        .replace("*", "0,999") \
        .replace("[0,]", "[0,999)") \
        .replace("[", "") \
        .replace(")", "") \
        .replace(" ", "")
    versions = ver.split(",")
    return versions[0], versions[1]


def in_between(version: str, vulnerable: [str]) -> bool:
    in_range = False
    for version_range in vulnerable:
        vr = get_versions(version_range)
        in_range = in_range or (vr[0] <= version < vr[1])
    return in_range
