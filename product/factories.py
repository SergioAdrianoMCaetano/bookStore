import factory
from product.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint', min_value=1, max_value=1000)  # Defina um intervalo para o preço
    category = factory.SubFactory(CategoryFactory)  # Usa SubFactory para criar uma Category associada
    title = factory.Faker('pystr')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.category.add(*extracted)

        # if extracted:
        #     for category in extracted:
        #         self.category.add(category)

    class Meta:
        model = Product
