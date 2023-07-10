# Python OCR

A proof of concept of a small OCR text recognition app using python + [tesseract-ocr](https://github.com/tesseract-ocr/tesseract) within [Docker](https://www.docker.com/)



## Prerequisites

- `docker@^24.0.3`

## How to use it?

1. Clone the repo executing `git clone git@github.com:dmmarmol/python-ocr.git`
2. Navigate into `cd python-ocr`
3. Run the command `make build` (Makefile shortcut to build the docker image)
4. Run the command `make run`
5. Run the command `make shell` to attach a shell to the running container
6. Choose between [bulk process images](#process-images) or [process text](#process-text)

### Process images

This command will read all images inside the `images/source` directory and will extract the text content from each of them putting them all together in a new file inside `images/output`

#### Steps

1. Deposit any `.jpg` or `jpeg` file inside `images/source` directory
2. Navigate inside the container using an attached shell and from the `app/` directory, run the command `python3 src/process-images.py`

### Process text

This command will read all `.txt` files inside the `text/source` directory and will normalize the text content from each of file putting them all together in a new file inside `text/output`

#### Steps

1. Deposit any `.txt` file inside `text/source` directory
2. Navigate inside the container using an attached shell and from the `app/` directory, run the command `python3 src/process-text.py`

## Commands

### Build

Build the Dockerfile image

```
make build
```

### Run

Run a docker container instance of the [Dockerimage](#build)

```
make run
```

### Restart docker container

```
make stop
make remove
```

Lastly, repeat [build](#build) and [run](#run) commands