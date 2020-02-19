import sqlalchemy

class HeavenAndHellDatabase:

    def __init__(self, engine, queries, table):
        self.engine = engine
        self.queries = queries
        self.table = table

    def create_table(self, engine, queries):
        for query in self.queries:
            engine.execute(query)

