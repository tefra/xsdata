@dataclass
class {{ name }}:
    {{'"""{}"""'.format(help) if help }}
{%- if fields|length == 0 %}
    pass
{% endif -%}
{% for field in fields %}
    {{ field.name }}: {{ field.type }} = field(
        {{- "default={}".format(repr(field.default)) if field.default is defined }}
        metadata={{ field.metadata }}
    )
{%- endfor %}
