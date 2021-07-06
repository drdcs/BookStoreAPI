from .db_objects import get_db_connection

async def execute(query: str, is_many: bool, values=None):
    """Based on the environment the db connection will be set.
    @Params: query: str -> SQL statement.
             is_many: boolean : True/False
             values: single or List of Values. 
    """
    db = get_db_connection()
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)


async def fetch(query: str, is_one: bool, values=None):
    """Based on the environment the db connection will be set.
       @Params: query: str -> SQL statement.
               is_one: boolean : True/False
               values: single or List of Values. 
    """
    db = get_db_connection()
    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            output = None
        else:
            output = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            output = None
        else:
            output = []
            for row in result:
                output.append(dict(row))
    return output