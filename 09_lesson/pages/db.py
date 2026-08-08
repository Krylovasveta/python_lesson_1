from sqlalchemy import create_engine, inspect, text


class Db:
    def __init__(self, con=None):
        self.con = con
        self.db_engine = None

    def db_con(self, login="postgres", password="svetakv", b="QA"):
        db_con_st = f"postgresql://{login}:{password}@localhost:5432/{b}"
        self.db_engine = create_engine(db_con_st)
        return self.db_engine

    def add_usr(self, id, email, subject):
        if not self.db_engine:
            self.db_con()
        with self.db_engine.connect() as con:
            con.execute(
                text(
                    "insert into users(user_id, user_email, subject_id) values (:id, :email, :subject)"
                ),
                {"id": id, "email": email, "subject": subject},
            )
            con.commit()

    def edit_usr(self, id, email):
        if not self.db_engine:
            self.db_con()
        with self.db_engine.connect() as con:
            con.execute(
                text("update users set user_email = :email where user_id= :id"),
                {"id": id, "email": email},
            )
            con.commit()

    def del_usr(self, id):
        if not self.db_engine:
            self.db_con()
        with self.db_engine.connect() as con:
            con.execute(text("delete from users where user_id= :id"), {"id": id})
            con.commit()

    def sel_usr(self, email):
        if not self.db_engine:
            self.db_con()
        with self.db_engine.connect() as con:
            c = con.execute(
                text("select * from users where user_email= :email"), {"email": email}
            )
            return c.mappings().all()

    def usr_lst(self):
        if not self.db_engine:
            self.db_con()
        i = inspect(self.db_engine)
        n = i.get_table_names()
        print(n)


# if __name__ == "__main__":
# db = Db()
# p = db.sel_usr("hroberts@yahoo.com")
# print(p)
# db.edit_usr(1, "sveta1@mail.ru")
# db.usr_lst()
