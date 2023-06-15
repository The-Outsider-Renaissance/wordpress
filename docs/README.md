# A Dummy WordPress Application

## Getting Started
- `bin/bootstrap`
- `bin/start`

- WordPress is available at http://localhost:8080/
- WordPress Admin is available at http://localhost:8080/wp/wp-admin/
- API is available at http://localhost:8000/

## Python User API

http://localhost:8000/ serves a FastAPI application

It interfaces with users with the following schema:

```py
class User(BaseModel):
    id: int = None # Auto-increment. Unmodifiable
    name: str
    title: str
    avatar: str
    is_active: Optional[bool] # Defaults to true
```

Some default users are provided by default when `bin/bootstrap` is run.

### API Routes

#### GET http://localhost:8000/users/

Returns list of all users in database

#### POST http://localhost:8000/users/

Provide JSON object payload to create a new user

Example:
- POST {"name":"Bob Jones","title":"Web Developer","avatar":"https://i.pravatar.cc/300"} => http://localhost:8000/users/

Returns created user

#### GET http://localhost:8000/users/{user_id}

Returns user matching user_id

#### PATCH http://localhost:8000/users/{user_id}

Modify provided user. Pass in JSON object as payload. All fields do not need to be provided.

Example:
- PATCH {"title": "New Title"} => http://localhost:8000/users/{user_id}

Returns modified user
