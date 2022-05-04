import sqlite3


def get_sql_connecting(query, params):
    """Подключаем базу данных SQL"""
    connect = sqlite3.connect("animal.db")
    cursor = connect.cursor()
    cursor.execute(query, params)
    executed_query = cursor.fetchall()
    connect.close()
    return executed_query

def get_animal_by_id(id):
    query = f"""
    SELECT * 
    FROM animals_finally
    WHERE id == :id
    """

    result = get_sql_connecting(query, {'id': f'{id}'})
    result_dict = {'id': result[0][0], 'age_upon_outcome': result[0][1], 'animal_id': result[0][2],
                   'animal_type': result[0][3], 'name': result[0][4], 'breed': result[0][5],
                   'dateOfBirth': result[0][6][0:10], 'outcome_id': result[0][7]
                   }
    return result_dict


def main():
    query_1 = """
        CREATE TABLE IF NOT EXISTS colors (
        id integer PRIMARY KEY AUTOINCREMENT,
        color varchar(50)
    )
    """

    query_2 = """
        CREATE TABLE IF NOT EXISTS animals_colors (
        animals_id integer,
        color_id integer,
        FOREIGN KEY (animals_id) REFERENCES animals_finally(id),
        FOREIGN KEY (color_id) REFERENCES colors(id)
    ) 
    """

    query_3 = """
        INSERT INTO colors(color)
        SELECT DISTINCT * FROM (
            SELECT DISTINCT color1 AS color FROM animals
            UNION
            SELECT DISTINCT color2 AS color FROM animals
        )
        DELETE FROM colors WHERE color IS NULL 
       
    """

    query_4 = """
        INSERT INTO animals_colors (animals_id, color_id)
        SELECT DISTINCT 
            animals_finally.id, colors.id  
        FROM animals
        JOIN colors ON colors.color = animals.color1
        JOIN animals_finally ON animals_finally.animal_id = animals.animal_id 
        UNION ALL 
        SELECT DISTINCT 
            animals_finally.id, colors.id  
        FROM animals 
        JOIN colors ON colors.color = animals.color2
        JOIN animals_finally ON animals_finally.animal_id = animals.animal_id         
           
        """


    query_5 = """
        CREATE TABLE IF NOT EXISTS outcome (
        id integer PRIMARY KEY AUTOINCREMENT,
        subtype varchar(50),
        "type" varchar(50),
        "month" integer,
        "year" integer
        )
        """

    query_6 = """
        INSERT INTO outcome(subtype, "type", "month", "year")
        SELECT DISTINCT 
            animals.outcome_subtype,
            animals.outcome_type,
            animals.outcome_month ,
            animals.outcome_year
        FROM animals 
            """

    query_7 = """
            CREATE TABLE IF NOT EXISTS animals_finally (
                id integer PRIMARY KEY AUTOINCREMENT,
                age_upon_outcome varchar(50),
                animal_id varchar(50),
                animal_type varchar(50),
                name varchar(50),
                breed varchar(50),
                date_of_birth varchar(50),
                outcome_id integer,
                FOREIGN KEY (outcome_id) REFERENCES outcome(id)
                )
                """



    query_8 = """
            INSERT INTO animals_finally (age_upon_outcome, animal_id, animal_type, name, breed, date_of_birth, outcome_id)
            SELECT DISTINCT 
                animals.age_upon_outcome,
                animals.animal_id ,
                animals.animal_type,
                animals.name,
                animals.breed,
                animals.date_of_birth,
                outcome.id 
            FROM animals  
            LEFT JOIN outcome ON outcome.subtype = animals.outcome_subtype
                        AND outcome."type" = animals.outcome_type
                        AND outcome."month" = animals.outcome_month
                        AND outcome."year" = animals.outcome_year
                """



