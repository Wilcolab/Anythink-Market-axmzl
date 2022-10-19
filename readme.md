# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup

- `git clone` the repo
- Run `docker-compose up` to load Anythink's backend and frontend.
- Check the backend is running and connected to the database: http://localhost:3000/api/ping
- Create a new user to check the frontend it’s connected to the backend: http://localhost:3001/register
