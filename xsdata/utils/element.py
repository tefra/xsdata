from xsdata.models.elements import Annotation, AnnotationBase, Documentation


def append_documentation(obj: AnnotationBase, string: str):
    if obj.annotation is None:
        obj.annotation = Annotation.build()
    if obj.annotation.documentation is None:
        obj.annotation.documentation = Documentation.build()
    if obj.annotation.documentation.text is None:
        obj.annotation.documentation.text = ""

    obj.annotation.documentation.text = "{}\n{}".format(
        obj.annotation.documentation.text, string
    ).strip()
