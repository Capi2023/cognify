# view.py

class Vista:
    @staticmethod
    def mostrar_menu_principal():
        print("Bienvenido al Sistema Cognify")
        print("1. Sentencia Tradicional")
        print("2. Rehabilitación Acelerada")
        return int(input("Seleccione una opción: "))

    @staticmethod
    def seleccionar_tipo_delito():
        print("Seleccione el tipo de delito:")
        print("1. Violento")
        print("2. Financiero")
        print("3. Odio")
        return int(input("Seleccione una opción: "))

    @staticmethod
    def mostrar_recuerdo(recuerdo):
        print("\n--- Recuerdo Asignado ---")
        print(f"Descripción: {recuerdo.descripcion}")
        print(f"Empatía: {'Sí' if recuerdo.empatia else 'No'}")
        print(f"Arrepentimiento: {'Sí' if recuerdo.arrepentimiento else 'No'}")
        print(f"Impacto: {recuerdo.impacto}")
