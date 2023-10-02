import asyncio
from db import aiomysql_CRUD

async def main():
    db = aiomysql_CRUD()
    await db.connect()

    # INSERT - The code performs an INSERT operation into the users table, inserting a record with the name "John Doe" and age 30.
    async def create_user(user_name, user_age):
        query = "INSERT INTO users (user_name, user_age) VALUES (%s, %s)"
        values = (user_name, user_age)
        await db.insert(query, values)

    # Now you can call the create_user function within an asynchronous context
    await create_user("John Doe", 35)


    # UPDATE - Updates a user's age to 55 based on their name ("John Doe").
    async def update_user(user_name, user_age):
        query = "UPDATE users SET user_age = %s WHERE user_name = %s"
        values = (user_age, user_name)  # Swap the values to match the order in the query
        await db.update(query, values)

    # This line of code calls the `update_user` function to change the age of a user named "John Doe" to 55 in the database.
    await update_user("John Doe", 55)


    # SELECT - This code defines a function `select_users_by_age` that retrieves users from the "users" table whose age is greater than the specified minimum age.
    # It then prints the selected users.
    async def select_users_by_age(min_age):
        query = "SELECT id, user_name, user_age FROM users WHERE user_age > %s"
        values = (min_age,)
        result = await db.select(query, values)
        return result

    min_age = 30  # Adjust this value to your desired minimum age
    users = await select_users_by_age(min_age)

    for user in users:
        print(user)

    # DELETE - Deleting a user from the users table based on their name.
    async def delete_user(user_name):
        query = "DELETE FROM users WHERE user_name = %s"
        values = (user_name,)
        await db.delete(query, values)


    # Calling the function to delete a user "John Doe" from the users table.
    await delete_user("John Doe")



    await db.close()

if __name__ == "__main__":
    asyncio.run(main())
