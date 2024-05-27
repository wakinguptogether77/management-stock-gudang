# Gudang data stok menggunakan dictionary
stock_data = {
    '0001': {'name': 'Bakso Tahu 500 Gram', 'quantity': 100, 'price': 32000},
    '0002': {'name': 'Pempek 450 Gram', 'quantity': 10, 'price': 31000},
    '0003': {'name': 'Dim Sum 500 Gram', 'quantity': 200, 'price': 80000}
}

# Data login untuk admin gudang
authorized_username = 'admin_gudang'
authorized_password = '@12345678'

def login():
    print("Login ke Sistem Manajemen Gudang Stok - Perusahaan Frozen Food")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username == authorized_username and password == authorized_password:
        print("Login berhasil! SELAMAT DATANG")
        return True
    else:
        print("Login gagal. Username atau password salah.")
        return False

def add_stock_item():
    # Input dari pengguna untuk data stok baru
    item_id = input("Masukkan ID barang: ")
    item_name = input("Masukkan nama barang: ")
    item_quantity = int(input("Masukkan jumlah barang: "))
    item_price = float(input("Masukkan harga barang: "))
    
    # Menambahkan data baru ke dictionary stock_data
    stock_data[item_id] = {
        'name': item_name,
        'quantity': item_quantity,
        'price': item_price
    }
    print("Barang berhasil ditambahkan.")

def update_stock_item():
    item_id = input("Masukkan ID barang yang ingin diubah: ")
    
    if item_id in stock_data:
        print(f"Data saat ini untuk ID {item_id}: {stock_data[item_id]}")
        
        print("Pilih kolom yang ingin diubah:")
        print("1. Nama")
        print("2. Jumlah")
        print("3. Harga")
        choice = input("Masukkan pilihan Anda: ")
        
        if choice == '1':
            new_name = input("Masukkan nama baru: ")
            stock_data[item_id]['name'] = new_name
        elif choice == '2':
            new_quantity = int(input("Masukkan jumlah baru: "))
            stock_data[item_id]['quantity'] = new_quantity
        elif choice == '3':
            new_price = float(input("Masukkan harga baru: "))
            stock_data[item_id]['price'] = new_price
        else:
            print("Pilihan tidak valid.")
        
        print("Data barang berhasil diperbarui.")
    else:
        print("ID barang tidak ditemukan.")

def delete_stock_item():
    item_id = input("Masukkan ID barang yang ingin dihapus: ")
    
    if item_id in stock_data:
        del stock_data[item_id]
        print("Barang berhasil dihapus.")
    else:
        print("ID barang tidak ditemukan.")

def display_stock():
    if not stock_data:
        print("Tidak ada data stok tersedia.")
    else:
        for item_id, item_info in stock_data.items():
            print(f"ID: {item_id}, Nama: {item_info['name']}, Jumlah: {item_info['quantity']}, Harga: {item_info['price']}")

def main():
    while not login():
        print("Silakan coba login kembali.")
    
    while True:
        print("\nSistem Manajemen Gudang Stok - CV Frozen Food")
        print("1. Tambah Barang Stok")
        print("2. Tampilkan Stok")
        print("3. Ubah Barang Stok")
        print("4. Hapus Barang Stok")
        print("5. Keluar")
        
        choice = input("Masukkan pilihan Anda: ")
        
        if choice == '1':
            add_stock_item()
        elif choice == '2':
            display_stock()
        elif choice == '3':
            update_stock_item()
        elif choice == '4':
            delete_stock_item()
        elif choice == '5':
            print("Keluar dari sistem. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()