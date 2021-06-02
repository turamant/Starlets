class SortKey:
    def __init__(self, *attribute_names):
        self.attribute_names = attribute_names

    def __call__(self, instance):
        values = []
        for attribute_name in self.attribute_names:
            values.append(getattr(instance, attribute_name))
        return values


class Person:
    def __init__(self, name, family, email):
        self.name = name
        self.family = family
        self.email =email



people = [Person("A", "A1", "A2"),
          Person("B", "B1", "B2"),
          Person("C", "C1", "C2")]

print(people.sort(key=SortKey("family")))
