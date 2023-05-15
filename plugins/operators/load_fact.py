from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    """
    Run SQL transformations to create fact table
    Input:
        redshift_conn_id
        table: target table
        sql_source: sql code to be run
        append mode: switching between insert/ truncate-insert pattern
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
                 append_mode=True,
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_source = sql_source
        self.append_mode = append_mode
        # Map params here
        # Example:
        # self.conn_id = conn_id

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)

        if not self.append_mode:
            redshift.run("DELETE FROM {}".format(self.table))

        formatted_sql = LoadFactOperator.insert_sql.format(
            self.table,
            self.sql_source
        )

        redshift.run(formatted_sql)
        self.log.info('LoadFactOperator implemented.')
