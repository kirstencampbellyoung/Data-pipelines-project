from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):
    """



    """

    ui_color = '#80BD9E'

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
                 table="",
                 sql_source="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_source = sql_source

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        redshift.run("DELETE FROM {}".format(self.table))

        formatted_sql = LoadDimensionOperator.insert_sql.format(
            self.table,
            self.sql_source
        )

        redshift.run(formatted_sql)

        self.log.info('LoadDimensionOperator not implemented yet')
