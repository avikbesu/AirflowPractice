def print_context(ds, **kwargs):
    """Print the Airflow context and ds variable from the context."""
    print(kwargs)
    print(ds)
    return 'Whatever you return gets printed in the logs'