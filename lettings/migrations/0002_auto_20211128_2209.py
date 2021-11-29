# Generated by Django 3.0 on 2021-11-28 22:09


from django.apps import apps as global_apps
from django.db import migrations


def add_data_in_table(apps, schema_editor):

    try:
        AddressOld = apps.get_model("oc_lettings_site", "Address")
    except LookupError:
        return

    AddressOld = apps.get_model("oc_lettings_site", "Address")
    AddressNew = apps.get_model("lettings", "Address")
    LettingNew = apps.get_model("lettings", "Letting")
    LettingOld = apps.get_model("oc_lettings_site", "Letting")

    for address_old in AddressOld.objects.all():
        address_new = AddressNew(
            number=address_old.number,
            street=address_old.street,
            city=address_old.city,
            state=address_old.state,
            zip_code=address_old.zip_code,
            country_iso_code=address_old.country_iso_code,
        )
        address_new.save()
        for letting_old in LettingOld.objects.filter(address=address_old):
            letting_new = LettingNew(title=letting_old.title, address=address_new)
            letting_new.save()


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_data_in_table),
    ]

    if global_apps.is_installed("oc_lettings_site"):
        dependencies.append(("oc_lettings_site", "0001_initial"))
