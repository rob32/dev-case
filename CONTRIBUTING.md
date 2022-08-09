# Contributor Guide

Thank you for your interest in improving DevCase.

The project is available under [GNU GPLv3](https://github.com/rob32/dev-case/blob/main/LICENSE.md) Licence and contributions, bug reports, feedback and feature-requests are always welcome.

In advance: Please make sure to branch from `develop`. The *main* branch serves as release bracnch for production.

## Bug Reports and Fixes

If you find a bug, please search for it in the [Issues](https://github.com/rob32/dev-case/issues), and if it isn't already tracked, create a new issue.

When creating a new Issue, please answer the following questions:

- Which operating system are you using?
- Which Python version are you using?
- Which version of DevCase are you using?
- What did you expect to see?
- What did you see instead?

## Feature Requests

Please check the [Roadmap](https://github.com/rob32/dev-case/blob/main/README.md#todoroadmap) before. Maybe the feature is already planned. Otherwise open an [Issue](https://github.com/rob32/dev-case/issues) and describes the feature you would like to see.

## Development Environment

Have a look at the instructions on the *Readme-Page* [Local Development](https://github.com/rob32/dev-case/blob/main/README.md#local-development).

## Tests

Run tests via:

```
python3 manage.py test
```

or with docker and docker-compose:

```
docker-compose exec web python manage.py test
```
## Code Formatting

DevCase uses `flake8`, `isort` and `black` for formatting and linting.
You can use `pre-commit` to check everything at once:

```
# to setup pre-commit
pre-commit install

# check code with
pre-commit run -a -v
```


## Pull Request

Open a [Pull Request](https://github.com/rob32/dev-case/pulls) to submit changes. Target branch should be `develop`, except for a hotfix.

Your pull request needs to meet the following guidelines for acceptance:

- The test suite must pass without errors and warnings.
- Formatting has been checked using `black` and `flake8`.
- Contains new UnitTests (not always the case).

It is recommended to open an [Issue](https://github.com/rob32/dev-case/issues) before starting to add new functionality to this project. This gives us the chance to talk about it and find an approach together.
