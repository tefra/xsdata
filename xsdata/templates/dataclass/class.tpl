@dataclass
class {{ obj.name }}{{"({})".format(obj.extends) if obj.extends }}:
    {{'"""{}"""'.format(obj.help) if obj.help }}
{%- if obj.attrs|length == 0 %}
    pass
{% endif -%}
{% for attr in obj.attrs %}
    {{ attr.name }}: {{ attr.type }} = field(
        {{- "default={},".format(attr.default) }}
        metadata={{ attr.metadata }}
    )
{%- endfor %}
