@dataclass
class {{ obj.name }}{{"({})".format(obj.extends) if obj.extends }}:
    {{'"""{}"""'.format(obj.help) if obj.help }}
{%- if obj.attrs|length == 0 %}
    pass
{% endif -%}
{% for attr in obj.attrs %}
    {{ attr.name }}: {{ 'List[{}]'.format(attr.type) if attr.is_list else attr.type }} = field(
        {{ "default_factory=list" if attr.is_list else "default={}".format(attr.default) }},
        metadata={{ attr.metadata }}
    )
{%- endfor %}
