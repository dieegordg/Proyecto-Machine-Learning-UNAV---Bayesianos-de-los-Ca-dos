def describe_corpus(df):
    """Devuelve descriptivos básicos del corpus."""
    return df.describe(include="all")
