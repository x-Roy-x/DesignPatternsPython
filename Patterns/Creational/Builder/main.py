text = "hello"
parts = ["<p>", text, "</p>"]

words = ['hello', 'world']

parts = ['<ul>']

for word in words:
    parts.append(f'\t<li>{word}</li>')

parts.append('</ul>')

from Patterns.Creational.Builder.builder import HtmlBuilder
from Patterns.Creational.Builder.builder_facets import PersonBuilder
from Patterns.Creational.Builder.builder_inheritance import PersonBirthDateBuilder

if __name__ == "__main__":
    print("\n".join(parts))

    builder = HtmlBuilder("ul")
    # builder.add_child("li", "Andrii")
    # builder.add_child("li", "Oleh")

    builder.add_child_fluent("li", "Roi").add_child_fluent("li", "text")

    print(builder)

    pb = PersonBuilder()

    person = pb \
        .lives \
        .at('123 London Road') \
        .in_city('London') \
        .works.at("Factory") \
        .earning(123000)\
        .build()

    print(person)

    pb2 = PersonBuilder().build()

    print(pb2)

    pb = PersonBirthDateBuilder()

    me = pb.called('Roi').born("07/12/99").works_as_a("Engineer").build()

    print(me)



