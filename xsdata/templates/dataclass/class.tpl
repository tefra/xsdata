{% set indent = indent|default(4) %}
@dataclass
class {{ obj.name }}{{"({})".format(obj.extends) if obj.extends }}:
    {{'"""{}"""'.format(obj.help) if obj.help }}
{%- if obj.attrs|length == 0 %}
    pass
{% endif -%}
{% for attr in obj.attrs %}
    {%- set display_type = '"{}"'.format(attr.type) if attr.forward_ref else attr.type %}
    {{ attr.name }}: {{ 'List[{}]'.format(display_type) if attr.is_list else display_type }} = field(
        {{ "default_factory=list" if attr.is_list else "default={}".format(attr.default) }},
        metadata={{ attr.metadata }}
    )
{%- endfor %}
{% for inner in obj.inner %}
    {%- filter indent(indent) -%}
    {%- with obj=inner, indent=indent+4 -%}
        {% include "class.tpl" %}
    {%- endwith -%}
    {%- endfilter -%}
{%- endfor -%}
