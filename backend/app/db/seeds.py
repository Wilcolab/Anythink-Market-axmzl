import asyncio
import random
import asyncpg
#from app.core.config import get_app_settings
from app.core.config import get_app_settings
from app.services.security import generate_salt, get_password_hash


async def seed_users(conn):
    """Seed 100 users."""
    for i in range(1, 101):
        username = f"user{i}"
        email = f"user{i}@example.com"
        password = "password123"
        salt = generate_salt()
        hashed_password = get_password_hash(salt + password)
        await conn.execute(
            "INSERT INTO users (username, email, salt, hashed_password) VALUES ($1, $2, $3, $4)",
            username, email, salt, hashed_password
        )
    print("Seeded 100 users.")


async def seed_items(conn):
    """Seed 100 items."""
    for i in range(1, 101):
        slug = f"item-{i}"
        title = f"Item {i}"
        description = f"Description for item {i}"
        body = f"Body content for item {i}"
        seller_id = random.randint(1, 100)
        await conn.execute(
            "INSERT INTO items (slug, title, description, body, seller_id) VALUES ($1, $2, $3, $4, $5)",
            slug, title, description, body, seller_id
        )
    print("Seeded 100 items.")


async def seed_comments(conn):
    """Seed 100 comments."""
    for i in range(1, 101):
        body = f"Comment {i} on this item."
        seller_id = random.randint(1, 100)
        item_id = random.randint(1, 100)
        await conn.execute(
            "INSERT INTO comments (body, seller_id, item_id) VALUES ($1, $2, $3)",
            body, seller_id, item_id
        )
    print("Seeded 100 comments.")


async def main():
    settings = get_app_settings()
    database_url = str(settings.database_url).replace("postgres://", "postgresql://")

    conn = await asyncpg.connect(database_url)
    try:
        async with conn.transaction():
            await seed_users(conn)
            await seed_items(conn)
            await seed_comments(conn)
        print("Database seeded successfully!")
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main())
