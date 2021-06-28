import os
import sys
import sqlite3 as sq
import time


# secondary functions ==================================================================================================

def current_directory() -> None:
    """to be sure that current working directory is located where *.py file is located"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())  # for debug purposes


def system_family_slash() -> str:
    """The function helps to create correct path
    https://docs.python.org/2/library/sys.html#platform
    """

    # print(sys.platform)  # for debug purposes

    if sys.platform.startswith('win'):
        return "\\"
    elif sys.platform.startswith('linux'):
        return "/"
    else:
        # !!! WARNING: the author is not familiar with path-building in other systems. Suppose it looks like linux
        return "/"


# main functions==================================================================================================

def create_database() -> object:
    """function creates a database named blog.sqlite in database folder in current working directory

    in the database creates table 'posts' with fields:
        - id INTEGER PRIMARY KEY AUTOINCREMENT,
        - title TEXT,
        - description TEXT,
        - date TEXT
    """
    current_directory()

    # the first creation folder for our databases
    if not os.path.exists(f"{os.getcwd()}{system_family_slash()}databases"):
        os.mkdir('databases')

    # creating database
    with sq.connect(f"databases{system_family_slash()}blog.sqlite") as connection:
        cursor = connection.cursor()

        # create table 'posts'
        cursor.execute("""CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT, 
        description TEXT, 
        date TEXT
        )""")

        connection.commit()

    return cursor


def select_all_posts() -> list:
    """function returns all post that exist in database"""

    with sq.connect(f"databases{system_family_slash()}blog.sqlite") as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM posts""")
        posts = cursor.fetchall()

        return posts


def add_new_post(title: str, description: str) -> None:
    """function adds a new post,
    required:
    title - text
    description - text
    """

    with sq.connect(f"databases{system_family_slash()}blog.sqlite") as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO posts  (title, description, date) VALUES '
                       f'("{title}", "{description}", "{time.ctime()}")')

        connection.commit()

    return None


def edit_post(identifier: int, title: str, description: str) -> None:
    """Function edit post
    required:
    identifier - int (filter)
    title - text
    description - text
    """

    with sq.connect(f"databases{system_family_slash()}blog.sqlite") as connection:
        cursor = connection.cursor()

        cursor.execute(f'UPDATE posts '
                        f'SET title = "{title}", description = "{description}"'
                        f'WHERE id = {identifier}')
        connection.commit()

    return None


def delete_post(identifier: int) -> None:
    """Function delete post
    required:
    identifier - int (filter)
    """

    with sq.connect(f"databases{system_family_slash()}blog.sqlite") as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM posts '
                        f'WHERE id = {identifier}')
        connection.commit()

    return None



def list_of_id() -> list:
    """create list od id, that needed while editing/deleting posts"""

    id_list = []
    posts = select_all_posts()

    for p in posts:
        id_list.append(p[0])

    return id_list


if __name__ == '__main__':
    pass
