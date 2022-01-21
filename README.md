# Example - Python/Flask
A template repository for jump-starting development of Python/Flask web services

## Development

### Create a Working Environment
Best practice is to create an isolated Python environment for each project
you work on to avoid dependency conflicts. I use conda in this project, but you
can use your preferred environment manager.

Create a conda environment from `environment.yml`:
```shell
conda env create --file environment.yml
```

Optionally you can choose your own name for the environment:
```shell
conda env create --file environment.yml --name <custom-name>
```

### Install Dependencies
This project requires third-party dependencies to function. If you used conda to
create an environment in [Create a Working Environment](#create-a-working-environment)
this has already been done for you.

Install dependencies required for development:
```shell
pip install -r requirements-dev.txt
```

> **Note:** When adding dependencies to the project, determine whether the
> dependency is needed for the operation this package or if it's only needed
> for ancillary development tasks (code style enforcement, test running, etc.).
> Necessary dependencies should be added to `requirements.txt`, ancillary
> dependencies should be added to `requirements-dev.txt`. You should always
> update `environment.yml` with the full list of development dependencies and
> their version. A more complete `requirements.txt` (or `requirements-prod.txt`)
> can be generated if you want to pin all version for all third-party
> dependencies.

### Run Tests
Tests are valuable for ensuring functionality doesn't break between releases.
This project uses `pytest` and related packages to perform unit tests.

All tests should pass before merging into a protected branch.

#### Using pytest
Run unit tests:
```shell
pytest
```

#### Checking Code Coverage
Code coverage is a metric for determining the maintainability of a project.

Run unit tests with code coverage:
```shell
pytest --cov=example
```

#### Generating Detailed Coverage Report
When assessing how to improve code coverage, it may be helpful to find which
lines are not being run during testing.

Run unit tests, check for code coverage, generate a browsable coverage report:
```shell
pytest --cov=example --cov-report=html
```

### Run the Service

#### Using Flask Development Server
Change into the `src/` directory:
```shell
cd src/
```

Set the FLASK_APP and LOG_LEVEL environment variables then start the service:
```shell
FLASK_APP=example.app \
LOG_LEVEL=INFO \
flask run
```

> The Flask development server should only be used in a development environment.
> You should front the service with a production-ready WSGI server (see
> [Using GUnicorn](#using-gunicorn)) and reverse proxy.

#### Using GUnicorn
Change into the `src/` directory:
```shell
cd src/
```

Set the LOG_LEVEL environment variable then start the service:
```shell
LOG_LEVEL=INFO \
gunicorn -b 0.0.0.0:5000 -w 2 "example.app:create_app()"
```

### Apply Code Formatting
Having a scripted code formatting tool improves readability and ensures
compliance with PEP. This project uses `black` to apply code style and
formatting.

Apply code formatting to all files in the `src/` directory:
```shell
python -m black --include src/* src/
```

Apply code formatting to all files in the `tests/` directory:
```shell
python -m black --include tests/* tests/
```

### Build Distributable Artifacts
Building projects into distributable artifacts helps simplify versioning,
improve compatibility, and enhance security. This project uses `build` to
simplify building binary distributable artifacts.

Build distributable artifacts:
```shell
python -m build
```

> This will output artifacts to the `dist/` directory. By default, this will
> create a source distribution and a wheel distribution.

Distributable artifacts can be uploaded to a Python package index. They can also
be installed directly via `pip`.

[//]: # (TODO: Write a "Upload to Package Index" section.)

Install from local `.whl` file:
```shell
pip install dist/example-0.1.0-py3-none-any.whl
```

Install from GitHub:
```shell
# Install from a .whl file hosted on a GitHub Release page
pip install https://github.com/BrimazOfOreskos/x-python-flask/releases/download/0.1.0/example-0.1.0-py3-none-any.whl

# Install the package as it exists on the default branch
pip install git+ssh://github.com/BrimazOfOreskos/x-python-flask.git

# Install the package as it exists on a specific branch or tag
pip install git+ssh://github.com/BrimazOfOreskos/x-python-flask.git@develop
pip install git+ssh://github.com/BrimazOfOreskos/x-python-flask.git@0.1.0

# Install the package as it exists at a specific commit
pip install git+ssh://github.com/BrimazOfOreskos/x-python-flask.git@c1f77a73923dbd93143c40cc7668832254651864
```

[//]: # (TODO: Write "Install from Package Index" section.)
