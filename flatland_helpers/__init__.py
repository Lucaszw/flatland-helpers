FIELD_TYPES = {}
FIELD_TYPES["number"] = ["Decimal", "Float", "Integer", "Long", "Number"]
FIELD_TYPES["string"] = ["String"]

NUMBER_VALIDATION = {}
NUMBER_VALIDATION["minimum"] = ["ValueAtLeast", "ValueBetween", "ValueLessThan"]
NUMBER_VALIDATION["maximum"] = ["ValueAtMost",  "ValueBetween", "ValueGreaterThan"]

STRING_VALIDATION = {}
STRING_VALIDATION["minLength"] = ["LongerThan",  "LengthBetween"]
STRING_VALIDATION["maxLength"] = ["ShorterThan", "LengthBetween"]

def flatlandToJSON(form):
    '''
    Convert Flatland Form Object to JSON schema
    '''
    step_fields = form().field_schema_mapping
    json_schema = {}

    for k, f in step_fields.iteritems():
        obj = {}
        field_type = f.__name__

        if field_type in FIELD_TYPES["number"]:
            obj["type"] = "number"

        if field_type is "Integer":
            obj["multipleOf"] = 1.0

        for v in f.validators:
            validator = type(v).__name__

            if (validator in NUMBER_VALIDATION["minimum"] and
                field_type in FIELD_TYPES["number"]):
                if hasattr(v, "minimum"):
                    obj["minimum"] = v.minimum
                if hasattr(v, "boundary"):
                    obj["minimum"] = v.boundary

            if (validator in NUMBER_VALIDATION["maximum"] and
                field_type in FIELD_TYPES["number"]):
                if hasattr(v, "maximum"):
                    obj["maximum"] = v.maximum
                if hasattr(v, "boundary"):
                    obh["minimum"] = v.boundary

            if (validator in STRING_VALIDATION["minLength"] and
                field_type in FIELD_TYPES["string"]):
                obj["minLength"] = v.minLength

            if (validator in STRING_VALIDATION["maxLength"] and
                field_type in FIELD_TYPES["string"]):
                obj["maxLength"] = v.maxLength

        json_schema[k] = obj

    return json.dumps(json_schema)
