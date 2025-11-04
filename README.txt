FastAPI Relationships Example (Users - Items - Profiles)
------------------------------------------------------
How to run (Windows):
1. Extract this folder.
2. Open folder in VS Code.
3. Make sure Docker Desktop is running.
4. Open terminal in the project folder and run:
   docker compose up --build
5. Open http://localhost:8000/docs to view and test APIs.

Endpoints:
- POST /users/         create user
- GET  /users/{id}     get user with items and profile
- GET  /users/         list users
- POST /items/         create item (owner_id required)
- GET  /items/         list items
- POST /profiles/      create profile (user_id required, one per user)
- GET  /profiles/{id}  get profile
