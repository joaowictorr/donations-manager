from src.donation import Donation
from src.persistence import save_donations, load_donations

def main():
    donations = load_donations()
    
    while True:
        print("\n--- GESTOR DE DOAÇÕES (SISTEMA ATIVO) ---")
        print("1. Registrar Nova Doação")
        print("2. Inventário Completo")
        print("3. Alertas de Validade")
        print("4. Sair")
        
        choice = input("Selecione uma opção: ")

        if choice == "1":
            try:
                name = input("Nome do Alimento: ")
                qty = input("Quantidade: ")
                exp = input("Validade (AAAA-MM-DD): ")
                new_donation = Donation(name, qty, exp)
                donations.append(new_donation)
                save_donations(donations)
                print("✓ Sucesso: Item registrado no sistema.")
            except Exception as e:
                print(f"❌ Erro de Validação: {e}")

        elif choice == "2":
            print("\n--- ESTOQUE ATUAL ---")
            for d in donations:
                print(f"• {d.item_name}: {d.quantity} un. | Validade: {d.expiration_date}")

        elif choice == "3":
            alerts = [d for d in donations if d.is_near_expiration()]
            if not alerts:
                print("✅ Tudo em dia! Nenhum item vence nos próximos 7 dias.")
            for d in alerts:
                print(f"⚠️ URGENTE: {d.item_name} vence em {d.expiration_date}!")

        elif choice == "4":
            print("Encerrando sistema...")
            break

if __name__ == "__main__":
    main()