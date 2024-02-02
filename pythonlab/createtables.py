import psycopg2
# This function tests to make sure that you can connect to the database


# This function sends an SQL query to the database
def create_table():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="szetob",
        user="szetob",
        password="pies457paper")

    cur = conn.cursor()

    sql1 = """
            DROP TABLE IF EXISTS us_cities; 
            CREATE TABLE us_cities (
                City text,
                State text, 
                Population real,
                lat real,
                lon real
            );
            """
    sql2 = """
            DROP TABLE IF EXISTS state_abv;
            CREATE TABLE state_abv (
                State text,
                Abbreviation text
            );
    """

    cur.execute( sql1 )
    cur.execute( sql2 )

    # fetchone() returns one row that matches your quer
    #row = cur.fetchone()

    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()
    #return row


create_table()