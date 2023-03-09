# Nork Town City

Application developed to control the number of cars that a person owns in Nork Town City.

## Requirements

`Python` with version 3.9 and `pip` with version 22.3.1
If you want to run docker container locally it will necessary to have at least version 20.10.6 from docker engine and docker-compose version 1.29.1

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Usage

You can use `docker-compose` to run the container based application:

```bash
docker-compose up web
```

Both approaches will expose the url [http://localhost:8000](http://localhost:8000).

## Friendly URLs

ApiFlask generates automatically some URLs for built-in services such as Swagger.

|Service|path|URL
|----|----|----|
|Swagger|/docs|[http://localhost/docs](http://localhost/docs)


## Contributing

Pull requests are welcome. If you want to change something, please respect the defined model

### Implementing a new feature

1. Clone this repository and then create a new branch from develop branch
2. Make and commit your changes
3. Open a pull request for develop branch and wait for review

`NOTE: main, homolog and develop branches are locked for directly push.`

## License

[MIT](https://choosealicense.com/licenses/mit/)
