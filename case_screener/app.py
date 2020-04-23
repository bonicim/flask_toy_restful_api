from case_screener import create_app
from case_screener.config import DevelopmentConfig

app = create_app(config=DevelopmentConfig)


@app.shell_context_processor
def make_shell_context():
    from case_screener.models import Case, db, CaseSchema

    return {"db": db, "Case": Case, "case_schema": CaseSchema()}
