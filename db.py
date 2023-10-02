import aiomysql

class aiomysql_CRUD:
    def __init__(self):
        self.pool = None

    async def connect(self):
        try:
            self.pool = await aiomysql.create_pool(
                host='localhost',
                user='root',
                password='Qwerty1234',
                db='my_base',
                maxsize=200,
                autocommit=True  # Adding the parameter autocommit=True.
            )
        except Exception as e:
            print(f"Database connection error: {e}")

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()

    async def delete(self, query, values):
        try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cur:
                        await cur.execute(query, values)
                        await conn.commit()
        except Exception as e:
            print(f"Delete query error: {e}")

    async def select(self, query, params):
        try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cur:
                        await cur.execute(query, params)
                        rows = await cur.fetchall()
                        return rows
        except Exception as e:
            print(f"Select query error: {e}")

    async def insert(self, query, values):
        try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cur:
                        await cur.execute(query, values)
                        await conn.commit()
        except Exception as e:
            print(f"Insert query error: {e}")

    async def update(self, query, values):
        try:
                async with self.pool.acquire() as conn:
                    async with conn.cursor() as cur:
                        await cur.execute(query, values)
                        await conn.commit()
        except Exception as e:
            print(f"Update query error: {e}")

    async def close(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
