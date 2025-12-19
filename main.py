from negocio.gestor_negocio import GestorNegocio
import sys

def main():
    gestor = GestorNegocio()
    usuario_activo = False

    while True:
        print("\n=== SISTEMA API POO ===")
        if not usuario_activo:
            print("1. Registrarse")
            print("2. Iniciar Sesión")
            print("3. Salir")
        else:
            print("--- MENU USUARIO ---")
            print("4. Traer datos de API (GET) y guardar en DB")
            print("5. Crear nuevo Post (POST)")
            print("6. Actualizar Post (PUT)")
            print("7. Eliminar Post (DELETE)")
            print("8. Cerrar Sesión")
        
        opcion = input("Seleccione: ")

        if opcion == "1":
            u = input("Usuario: ")
            p = input("Contraseña: ")
            gestor.registrar_usuario(u, p)
        
        elif opcion == "2":
            u = input("Usuario: ")
            p = input("Contraseña: ")
            if gestor.login(u, p):
                print(f"¡Bienvenido {u}!")
                usuario_activo = True
            else:
                print("Credenciales incorrectas.")

        elif opcion == "3":
            sys.exit()

        elif usuario_activo:
            if opcion == "4":
                gestor.sincronizar_api()
                gestor.mostrar_locales()
            elif opcion == "5":
                t = input("Título: ")
                b = input("Cuerpo: ")
                gestor.api.post_data({"title": t, "body": b, "userId": 1})
            elif opcion == "6":
                i = input("ID a modificar: ")
                t = input("Nuevo Título: ")
                gestor.api.put_data(i, {"title": t, "userId": 1})
            elif opcion == "7":
                i = input("ID a eliminar: ")
                gestor.api.delete_data(i)
            elif opcion == "8":
                usuario_activo = False

if __name__ == "__main__":
    main()