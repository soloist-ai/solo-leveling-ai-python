import io
from fastavro import schemaless_writer, schemaless_reader


def avro_serialize(obj, schema):
    buf = io.BytesIO()
    schemaless_writer(buf, schema, obj)
    return buf.getvalue()


def avro_deserialize(data, schema):
    buf = io.BytesIO(data)
    return schemaless_reader(buf, schema)
