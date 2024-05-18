import re,datetime


class joi:

    def __init__(self, joi):
        self.joi = joi

    def get_joi(self):
        return self.joi

    def get_keys(self):
        return [i for i in self.joi.keys()]

    def check_string_properties(self, form, key, form_keys) -> bool:
        field_keys = [i for i in self.joi[key].keys()]
        properties_exists = "minlength" in field_keys or "maxlength" in field_keys
        return (key in form_keys and isinstance(form[key], self.joi[key]["type"])
                and type(form[key]) in [str] and properties_exists)

    def check_max_and_min_for_numbers(self, form, key, form_keys) -> bool:
        field_keys = [i for i in self.joi[key].keys()]
        max_or_min_exists = "min" in field_keys or "max" in field_keys
        return (key in form_keys and isinstance(form[key], self.joi[key]["type"])
                and type(form[key]) in [int, float] and max_or_min_exists)

    def check_regex(self, form, key, form_keys) -> bool:
        field_keys = [i for i in self.joi[key].keys()]
        is_regex_exists = "regex" in field_keys
        return (key in form_keys and isinstance(form[key], self.joi[key]["type"])
                and type(form[key]) in [str] and is_regex_exists)

    def check_date(self, form, key, form_keys) -> bool:
        field_keys = [i for i in self.joi[key].keys()]
        is_date_format = "format" in field_keys and "dateformat" in field_keys and self.joi[key]["format"] == "date"
        return (key in form_keys and isinstance(form[key], self.joi[key]["type"])
                and type(form[key]) in [str] and is_date_format)

    def validate(self, form):
        missing_fields = []
        wrong_field = []
        base_form_keys = self.get_keys()
        form_keys = [i for i in form.keys()]
        for key in base_form_keys:
            if key in form_keys and not isinstance(form[key], self.joi[key]["type"]):
                wrong_field.append({
                    f"{key}": {
                        "message": "wrong type"
                    }
                })
            elif self.check_max_and_min_for_numbers(form, key, form_keys):
                field_keys = [i for i in self.joi[key].keys()]
                if "max" in field_keys and form[key] > self.joi[key]["max"]:
                    wrong_field.append({
                        f"{key}": {
                            "message": "wrong filed , the value is bigger than maximum"
                        }
                    })
                elif "min" in field_keys and form[key] < self.joi[key]["min"]:
                    wrong_field.append({
                        f"{key}": {
                            "message": "wrong filed , the value is smaller than minimum"
                        }
                    })
            elif self.check_regex(form, key, form_keys):
                regexp = self.joi[key]["regex"]
                result_regex = re.match(regexp, form[key])
                if not result_regex:
                    wrong_field.append({
                        f"{key}": {
                            "message": f"{key} is not a correct format"
                        }
                    })
            elif self.check_string_properties(form, key, form_keys):
                field_keys = [i for i in self.joi[key].keys()]
                if "maxlength" in field_keys and len(form[key]) > self.joi[key]["maxlength"]:
                    wrong_field.append({
                        f"{key}": {
                            "message": f"{key} is too long"
                        }
                    })
                elif "minlength" in field_keys and len(form[key]) < self.joi[key]["minlength"]:
                    wrong_field.append({
                        f"{key}": {
                            "message": f"{key} is too short"
                        }
                    })

            elif self.check_date(form, key, form_keys):
                field_keys = [i for i in self.joi[key].keys()]
                date = None

                try:
                    date = datetime.strptime(form[key], self.joi[key]["dateformat"])
                except Exception as e:
                    wrong_field.append({
                        f"{key}": {
                            "message": f"{key} is not a correct format"
                        }
                    })

                if date is not None and "min" in field_keys and isinstance(self.joi[key]["min"],datetime) and date < self.joi[key]["min"]:
                    wrong_field.append({
                        f"{key}": {
                            "message": f"{key} is lower than the minimum"
                        }
                    })
                if date is not None and "max" in field_keys and isinstance(self.joi[key]["max"],datetime) and date > self.joi[key]["max"]:
                    wrong_field.append({
                        f"{key}": {
                            "message": f"{key} is higher than the maximum"
                        }
                    })

            elif self.joi[key].get("required", False) and key not in form_keys:
                missing_fields.append({
                    f"{key}": {
                        "message": "missing required field"
                    }
                })

        for key in form_keys:
            if key not in base_form_keys:
                wrong_field.append({
                    f"{key}": {
                        "message": "wrong key"
                    }
                })

        form_accepted = (len(missing_fields) == 0 and len(wrong_field) == 0)

        return dict(accepted=form_accepted, missing_fields=missing_fields, wrong_field=wrong_field)
    


class joiobject:

    def __init__(self):
        self.object = {}

    def string(self):
        self.object['type'] = str
        return self

    def integer(self):
        self.object['type'] = int
        return self

    def float(self):
        self.object['type'] = float
        return self

    def boolean(self):
        self.object['type'] = bool

    def datetime(self):
        self.object['type'] = datetime
        return self

    def type(self, value):
        self.object['type'] = value
        return self

    def required(self):
        self.object['required'] = True
        return self

    def optional(self):
        self.object['required'] = False
        return self

    def min(self, value):
        self.object['min'] = value
        return self

    def max(self, value):
        self.object['max'] = value
        return self

    def format(self, value):
        self.object['format'] = value
        return self

    def dateformat(self, value):
        self.object['dateformat'] = value
        return self

    def get(self):
        return self.object
    
    def maxlength(self, value):
        self.object['maxlength'] = value
        return self
    
    def minlength(self, value):
        self.object['minlength'] = value
        return self
