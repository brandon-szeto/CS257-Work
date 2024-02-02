import psycopg2
# This function sends an SQL query to the database
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="szetob",
        user="szetob",
        password="pies457paper")

    if conn is not None:
        print( "Connection Worked!" )
        return conn #Returns the connection if it was succesful
    else:
        print( "Problem with Connection" )

    return None

#This sees if Northfield is within the database, if it is it will print its latitude and longitude
#If it isn't, it will print a message saying Northfield is not in the database
def query_northfield(conn):

    cur = conn.cursor()

    sql = "SELECT lat, lon FROM us_cities WHERE City = 'Northfield'"
    cur.execute( sql )
    # fetchone() returns one row that matches your quer
    row = cur.fetchone()

    if row:
        print("Northfield's latitude and longitude is: ", row[0], row[1])
    else:
        print("Northfield is not in the database.")

    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()  
    return row

#This will print the city with the largest population
def query_population_max(conn):
    cur = conn.cursor()

    sql = "SELECT City FROM us_cities WHERE Population = (SELECT MAX(Population) FROM us_cities)"
    cur.execute(sql)
    row = cur.fetchone()

    if row:
        print("The city with the biggest population is: ", row[0])
    else:
        #This message should never pop up
        print("There is no city with the biggest population")

        conn.commit()
        return row

#This will print out the city with the smallest population
def query_population_min(conn):
    cur = conn.cursor()

    sql = "SELECT City FROM us_cities WHERE Population = (SELECT MIN(Population) FROM us_cities)"
    cur.execute(sql)
    row = cur.fetchone()

    if row:
        print("The city with the smallest population is: ", row[0])
    else:
        #This message should never pop up
        print("There is no city with the smallest population")
        conn.commit()
        return row

#This will print out the cities furtherest North, South, East, West
def query_farthest_cities(conn):
    cur = conn.cursor()

    sql_north = "SELECT City FROM us_cities WHERE lat = (SELECT MAX(lat) FROM us_cities)"
    sql_south = "SELECT City FROM us_cities WHERE lat = (SELECT MIN(lat) FROM us_cities)"
    sql_east = "SELECT City FROM us_cities WHERE lon = (SELECT MAX(lon) FROM us_cities)"
    sql_west = "SELECT City FROM us_cities WHERE lon = (SELECT MIN(lon) FROM us_cities)"
    cur.execute(sql_north)
    row_north = cur.fetchone()
    cur.execute(sql_south)
    row_south = cur.fetchone()
    cur.execute(sql_east)
    row_east = cur.fetchone()
    cur.execute(sql_west)
    row_west = cur.fetchone()
    if row_north:
        print("The furthest north city is: ", row_north[0])
    else:
        print("No city found.")

    if row_south:
        print("The furthest south city is: ", row_south[0])
    else:
        print("No city found.")
    
    if row_east:
        print("The furthest east city is: ", row_east[0])
    else:
        print("No city found.")

    if row_west:
        print("The furthest west city is: ", row_west[0])
    else:
        print("No city found.")

    cur.close()
    return row_north, row_south, row_west, row_east

#This will print the total population of a city

#This part of the code will get the full name of the city
def get_full_name(conn, state_input):
    cur = conn.cursor()
    sql_abv = "SELECT State FROM state_abv WHERE Abbreviation = %s"

    # (state_input,): This is a tuple containing the value(s) to be substituted for the parameter(s) in the SQL query. 
    # In this case, there is one parameter, so it's a tuple with one element. 
    # The comma at the end is necessary to indicate that it's a tuple with a single element;
    # otherwise, Python would interpret the parentheses as grouping parentheses rather than creating a tuple.
    cur.execute(sql_abv, (state_input,))
    row = cur.fetchone()
    if row:
        return row[0]
    return None


def query_state_pop(conn):
    state_input = input("Please enter a state name or abbreviation that you would like to know the population of: ")
    cur = conn.cursor()
    sql = "SELECT Population FROM us_cities WHERE Abbreviation = %s"
    cur.execute(sql, (state_input,))
    abbreviation_exists = cur.fetchone()[0]

    if abbreviation_exists:
        full_state_name = get_full_name(conn, state_input)
    else:
        full_state_name = state_input

    sql_pop = "SELECT SUM(population) FROM us_cities WHERE State = %s"
    cur.execute(sql_pop, (full_state_name,))
    total_population = cur.fetchone()[0]

    if total_population:
        print(f"Total population of all cities in {full_state_name}: {total_population}")
    else:
        print(f"No population data found for {full_state_name}")

    cur.close()




test_connection()
query_northfield()
query_population_max()
query_population_min()
query_state_pop()










