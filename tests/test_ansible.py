import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


def test_prom2teams_user(User, Group, AnsibleDefaults):
    user = User(AnsibleDefaults["prom2teams_user"])
    group = Group(AnsibleDefaults["prom2teams_group"])

    assert user.exists
    assert group.exists
    assert user.group == AnsibleDefaults["prom2teams_group"]


def test_prom2teams_version(PipPackage, AnsibleDefaults):
    installed_packages = PipPackage.get_packages(pip_path='/usr/bin/pip3')

    expected_version = AnsibleDefaults["prom2teams_version"]
    installed_version = installed_packages["prom2teams"]["version"]

    assert installed_version == expected_version


def test_prom2teams_service(File, Service, Socket, AnsibleDefaults):
    prom2teams_port = AnsibleDefaults["prom2teams_port"]

    assert Socket("tcp://0.0.0.0:{0}".format(prom2teams_port)).is_listening
    assert File("/lib/systemd/system/prom2teams.service").exists
    assert Service("prom2teams").is_enabled
    assert Service("prom2teams").is_running
