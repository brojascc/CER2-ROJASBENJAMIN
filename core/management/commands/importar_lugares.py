import csv
from django.core.management.base import BaseCommand
from core.models import LugarPatrimonial, Categoria


class Command(BaseCommand):
    help = "Importa lugares patrimoniales desde un CSV (categorías ya existentes)"

    def add_arguments(self, parser):
        parser.add_argument("archivo", type=str)

    def handle(self, *args, **options):
        creados = actualizados = 0
        with open(options["archivo"], newline="", encoding="utf-8-sig") as f:
            for fila in csv.DictReader(f):
                try:
                    # Si tu campo no se llama "nombre", cámbialo aquí
                    categoria = Categoria.objects.get(nombre=fila["categoria"])
                except Categoria.DoesNotExist:
                    self.stderr.write(f"Categoría no encontrada: {fila['categoria']} ({fila['nombre']})")
                    continue

                _, creado = LugarPatrimonial.objects.update_or_create(
                    nombre=fila["nombre"],
                    defaults={
                        "descripcion": fila["descripcion"],
                        "ubicacion": fila["ubicacion"],
                        "anio_construccion": fila["anio_construccion"] or None,
                        "imagen": fila["imagen"] or None,
                        "categoria": categoria,
                    },
                )
                creados += creado
                actualizados += not creado
        self.stdout.write(self.style.SUCCESS(f"Listo: {creados} creados, {actualizados} actualizados"))