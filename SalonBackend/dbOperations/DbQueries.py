

class DbQueries:
    @staticmethod
    def select_query(columns, condition_column, condition):
        return "Select "+columns+" where "+condition_column+" = "+condition+";"

    # @staticmethod
    # def get_query(columns, conditionColumn, condition):
    #     return "Select " + columns + " where " + conditionColumn + " = " + condition

    @staticmethod
    def insert_query(table_name, columns_name, values):
        return "insert into "+table_name+" ("+columns_name+") values("+values+");"

    @staticmethod
    def delete_query( table_name, condition_column, condition):
        return "delete from "+table_name+" where "+condition_column+" = "+condition+";"

