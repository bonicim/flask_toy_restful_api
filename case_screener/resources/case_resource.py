from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from case_screener.models import db, Case, CaseSchema

case_schema = CaseSchema()


class CaseResource(Resource):
    def post(self):
        case = self._create_case()
        self._save_case(case)
        screened_case = self._screen_case(case)
        self._update_case(screened_case)
        self._notify_lawyers(screened_case)
        return self._acknowledge_client(screened_case)

    def _create_case(self):
        case = Case()
        try:
            case_data = request.form
            case = case_schema.load(
                case_data
            )  # Schema handles input validation for free
        except ValidationError as err:
            print(err.messages)
            print(err.valid_data)

        return case

    def _save_case(self, case):
        db.session.add(case)
        db.session.commit()

    def _screen_case(self, case):
        if not case.viable:
            return case
        # TODO: add logic of screening cases
        return case

    def _update_case(self, case):
        if not case.viable:
            return case
        # TODO: Update case's viable and rating properties
        return case

    def _notify_lawyers(self, case):
        # TODO: Add API to lawyer messaging service
        if case.viable:
            pass
        pass

    def _acknowledge_client(self, case):
        msg = (
            f"Hi {case.name}. Your case, caseId {case.id} has successfully processed. "
            f"We will get back to you soon. Thanks and have a nice day."
        )
        return {"msg": msg}
