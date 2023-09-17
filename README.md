# Server-Sent Events (SSE) Demo with FastAPI

This is a simple demonstration of Server-Sent Events (SSE) using FastAPI. It provides a minimalistic frontend that displays real-time updates from the server in a table format.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

Server-Sent Events (SSE) is a web technology that allows servers to push real-time updates to web clients over a single HTTP connection. In this project, we use FastAPI to create a simple SSE server and provide a frontend for visualizing the real-time updates.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/AndreyKlychnikov/fastapi-sse.git
   ```

2. Navigate to the project directory:

   ```shell
   cd sse-fastapi-demo
   ```

3. Install the required Python dependencies using `poetry`:

   ```shell
   poetry install
   ```

## Usage

1. Start the FastAPI application:

   ```shell
   uvicorn main:app --reload
   ```

   The application will be accessible at [http://localhost:8000](http://localhost:8000).

2. Open a web browser and visit [http://localhost:8000](http://localhost:8000) to see the SSE demo in action. The page will display real-time updates in a table format.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
