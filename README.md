![Logo](https://raw.githubusercontent.com/idealista/prom2teams_role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/prom2teams_role.png)](https://travis-ci.org/idealista/prom2teams_role)

# prom2teams Ansible role

This Ansible role installs prom2teams in a Debian environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [prom2teams](https://github.com/idealista/prom2teams) server in a Debian system.

### Prerequisities

Ansible >=2.9 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver. Pipenv >=2018.11.26 and Python 3 recommended.

### Installing

Create or add to your roles dependency file (e.g requirements.yml) from GitHub:

```
- src: http://github.com/idealista/prom2teams_role.git
  scm: git
  version: 2.4.0
  name: prom2teams
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/prom2teams_role/) as origin if you prefer:

```
- src: idealista.prom2teams_role
  version: 2.4.0
  name: prom2teams
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: prom2teams }
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

Mandatory property is `prom2teams_webhook_urls`. For example:

```
prom2teams_webhook_urls:
  connector1: http://test
  connector2: http://test2
```

## Testing

```
pipenv shell
pipenv sync
molecule test
```

See `molecule.yml` to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-4.8.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/prom2teams_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/prom2teams_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
