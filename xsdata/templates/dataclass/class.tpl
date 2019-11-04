@dataclass
class {{ obj.name }}{{"({})".format(obj.extends) if obj.extends }}:
    {{'"""{}"""'.format(obj.help) if obj.help }}
{%- if obj.fields|length == 0 %}
    pass
{% endif -%}
{% for field in obj.fields %}
    {{ field.name }}: {{ field.type }} = field(
        {{- "default={},".format(field.default) }}
        metadata={{ field.metadata }}
    )
{%- endfor %}
