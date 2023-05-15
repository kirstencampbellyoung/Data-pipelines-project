from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    """
    With dimension and fact operators, you can utilize the provided SQL helper class to run data transformations. Most of the logic is within the SQL transformations and the operator is expected to take as input a SQL statement and target database on which to run the query against. You can also define a target table that will contain the results of the transformation.
    Dimension loads are often done with the truncate-insert pattern where the target table is emptied before the load. Thus, you could also have a parameter that allows switching between insert modes when loading dimensions. Fact tables are usually so massive that they should only allow append type functionality.

    runs transformation sql queries against target database to create fact table
    input:
        ..
        .
    output:
        ll:
        ll:
    """

    ui_color = '#F98866'

    insert_sql = """
        INSERT INTO {}
        {}
        ;
    """

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id="",
                 table = "",
                 sql_source="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_source = sql_source
        # Map params here
        # Example:
        # self.conn_id = conn_id

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)

        redshift.run("DELETE FROM {}".format(self.table))

        formatted_sql = LoadFactOperator.insert_sql.format(
            self.table,
            self.sql_source
        )

        redshift.run(formatted_sql)
        self.log.info('LoadFactOperator implemented.')
