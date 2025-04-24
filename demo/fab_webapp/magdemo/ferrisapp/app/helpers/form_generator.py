from flask_wtf import FlaskForm
from wtforms import Form
from wtforms.fields import (
    DecimalField,
    FileField,
    FloatField,
    IntegerField,
    RadioField,
    SelectField,
    SelectMultipleField,
    StringField,
    TextAreaField,
)


class FormGenerator:
    type2field = {
        "text": StringField,
        "textarea": TextAreaField,
        "int": IntegerField,
        "float": FloatField,
        "decimal": DecimalField,
        "select": SelectField,
        "multiselect": SelectMultipleField,
        "radio": RadioField,
        "file": FileField,
    }

    def __init__(self):
        pass

    @staticmethod
    def generate(params):
        class F(Form):
            pass

        for f in params.get("fields", []):
            setattr(F, f["name"], FormGenerator._get_field(f))

        return F()

    @staticmethod
    def _get_field(field):
        html_attributes = ["min", "max", "value", "step", "placeholder"]

        render_kw = {}

        for attr in html_attributes:
            if field.get(attr, None):
                render_kw[attr] = field[attr]

        for k, v in field.get("data", {}).items():
            render_kw[f"data-{k}"] = v

        if field.get("required", False):
            render_kw["required"] = "required"

        if field["type"] != "radio":
            render_kw["class"] = "form-control"

        if field["type"] in ["int", "decimal", "float"]:
            render_kw["type"] = "number"

        kwargs = dict(
            id=f"generated-{field['type']}-field",
            label=field["label"],
            default=field.get("default", None),
            description=field.get("description", ""),
            _name=field["name"],
            render_kw=render_kw,
        )

        if "choices" in field:
            kwargs["choices"] = [(i["value"], i["title"]) for i in field.get("choices", [])]

        return FormGenerator.type2field[field["type"]](**kwargs)
